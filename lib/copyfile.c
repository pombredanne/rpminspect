/*
 * Copyright 2003-2018 David Cantrell <david.l.cantrell@gmail.com>
 *                     David Shea <david@reallylongword.org>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @file copyfile.c
 * @author David Cantrell &lt;david.l.cantrell@gmail.com&gt;
 * @author David Shea &lt;david@reallylongword.org&gt;
 * @date 2003-2018
 * @brief Generic file copy function
 * @copyright Apache-2.0
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <libgen.h>
#include <limits.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <assert.h>
#include "rpminspect.h"

/**
 * @brief Generic file copy function.
 *
 * copyfile() is suitable for use in the callback for functions like
 * ftw() and nftw().  You must specify the source and destination and
 * the function only works on files.  Errors are reported on stderr.
 *
 * @param src Full path to source file.
 * @param dest Full path to the destination file.
 * @param force True to force overwriting the destination if it
 *              already exists, false otherwise.
 * @param verbose True to output verbose messages to stdout during the
 *                copy operation, false otherwise.
 * @return 0 on success, -1 on error.
 */
int copyfile(const char *src, const char *dest, bool force, bool verbose) {
    FILE *in = NULL, *out = NULL;
    int out_fd;                 /* use open() to test if file exists, then
                                 * fdopen for out */
    char buf[BUFSIZ];
    size_t s;
    int success = 0;
    char *destpath = NULL;
    char *destdir = NULL;
    char linkdest[PATH_MAX + 1];
    int oflags = O_WRONLY | O_CREAT | O_EXCL;
    mode_t mode = (S_IRWXU | S_IRGRP | S_IROTH) ^ S_IXUSR;
    struct stat sb;

    assert(src != NULL);
    assert(dest != NULL);

    /* stat the source */
    if (lstat(src, &sb) == -1) {
        fprintf(stderr, _("*** Unable to stat %s: %s\n"), src, strerror(errno));
        fflush(stderr);
        return -1;
    }

    /* create destination directory if it doesn't exist */
    destpath = strdup(dest);
    destdir = dirname(destpath);

    if (mkdirp(destdir, S_IRWXU) == -1) {
        fprintf(stderr, _("*** Unable to create directory %s: %s\n"), destdir, strerror(errno));
        fflush(stderr);
        return -1;
    }

    free(destpath);

    /* if src is a symlink, handle it here */
    if (S_ISLNK(sb.st_mode)) {
        if (readlink(src, linkdest, PATH_MAX) == -1) {
            fprintf(stderr, _("*** Unable to read symlink info on %s: %s\n"), src, strerror(errno));
            fflush(stderr);
            return -1;
        }

        if (symlink(linkdest, dest) == -1) {
            fprintf(stderr, _("*** Unable to create symlink %s: %s\n"), dest, strerror(errno));
            fflush(stderr);
            return -1;
        }

        return 0;
    }

    /* copy src to dest */
    if ((in = fopen(src, "r")) == NULL) {
        fprintf(stderr, _("*** Unable to open %s for reading: %s\n"), src, strerror(errno));
        fflush(stderr);
        return -1;
    }

    if ((out_fd = open(dest, oflags, mode)) == -1) {
        if (errno == EEXIST) {
            if (verbose) {
                fprintf(stderr, _("*** %s already exists"), dest);
                fflush(stderr);
            }

            if (force) {
                if (verbose) {
                    fprintf(stderr, _(", overwriting\n"));
                    fflush(stderr);
                }

                if (remove(dest)) {
                    fprintf(stderr, _("*** Unable to remove %s: %s\n"), dest, strerror(errno));
                    fflush(stderr);
                    return -1;
                } else {
                    if ((out_fd = open(dest, oflags, mode)) == -1) {
                        fprintf(stderr, _("*** Still unable to open %s, giving up\n"), dest);
                        fflush(stderr);
                    }
                }
            } else {
                putc('\n', stderr);
                fflush(stderr);
                return -1;
            }
        } else {
            fprintf(stderr, _("*** Unable to open %s for writing: %s\n"), dest, strerror(errno));
            fflush(stderr);
            return -1;
        }
    }

    if ((out = fdopen(out_fd, "wb")) == NULL) {
        fprintf(stderr, _("*** Unable to open %s: %s\n"), dest, strerror(errno));
        fflush(stderr);
        return -1;
    }

    while ((s = fread(buf, sizeof(char), BUFSIZ, in)) > 0) {
        if (fwrite(buf, sizeof(char), s, out) != s) {
            fprintf(stderr, _("*** Error writing to %s: %s\n"), dest, strerror(errno));
            fflush(stderr);
            errno = 0;
            success = -1;
            break;
        }
    }

    if (fflush(out) | fclose(out)) {
        fprintf(stderr, _("*** Error writing to %s: %s\n"), dest, strerror(errno));
        fflush(stderr);
        success = -1;
    }

    fclose(in);

    if (success != 0) {
        remove(dest);
    }

    /* set ownerships and permissions */
    if (geteuid() == 0) {
        if (chown(dest, sb.st_uid, sb.st_gid) == -1) {
            fprintf(stderr, _("*** chown() error on %s: %s\n"), dest, strerror(errno));
            fflush(stderr);
            success = -1;
        }
    }

    if (chmod(dest, (sb.st_mode & (S_ISUID | S_ISGID | S_ISVTX | S_IRWXU | S_IRWXG | S_IRWXO))) == -1) {
        fprintf(stderr, _("*** chmod() error on %s: %s\n"), dest, strerror(errno));
        fflush(stderr);
        success = -1;
    }

    return success;
}
