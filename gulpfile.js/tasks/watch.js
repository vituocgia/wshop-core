var gulp = require('gulp');

gulp.task('watch', function() {
    var watch = require('gulp-watch');

    gulp.watch('src/wshop/static/wshop/less/**/*.less', ['less']);
});
