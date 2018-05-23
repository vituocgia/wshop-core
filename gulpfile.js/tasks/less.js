var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    pump = require('pump'),
    less_task = function(cb) {
        pump([
            gulp.src('src/wshop/static/wshop/less/*.less'),
            sourcemaps.init(),
            less({includePaths: [
                    'src/wshop/static/less/',
                    ],
                    outputStyle: null,
                }),
            sourcemaps.write('/'),
            gulp.dest('src/wshop/static/wshop/css/')
            ],
            cb
        );
    };

gulp.task('less', less_task);
