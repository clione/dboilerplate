module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    // Concatanation of JS
    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: [
          '<%= pkg.project_paths.scripts_folder %>bower_components/jquery/jquery.js',
          '<%= pkg.project_paths.scripts_folder %>bower_components/foundation/js/foundation.min.js',
          '<%= pkg.project_paths.project_folder %>js/*.js'
        ],
        dest: '<%= pkg.dest_paths.js %><%= pkg.name %>.js'
      }
    },
    // Minification of JS
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          '<%= pkg.dest_paths.js %><%= pkg.name %>.min.js': ['<%= concat.dist.dest %>'],
          '<%= pkg.dest_paths.js %>modernizr.min.js': ['<%= pkg.project_paths.scripts_folder %>bower_components/modernizr/modernizr.js']
        }
      }
    },
    // JSHint to review JS code before build
    jshint: {
      files: [
        '<%= pkg.project_paths.project_folder %>js/*.js',
        '<%= pkg.project_paths.project_folder %>js/components/*.js'
      ],
      options: {
        // options here to override JSHint defaults
        globals: {
          jQuery: true,
          console: true,
          module: true,
          alert: true,
          document: true
        }
      }
    },
    // Compass to handle CSS compilation and concatanation
    compass: {
      dist: {
        options: {
          config: "config.rb"
        }
      }
    },
    // Watch task to compile files live
    watch: {
      js:{
        files: ['<%= jshint.files %>'],
        tasks: ['jshint']
      },
      scss: {
        files: ['<%= pkg.src_paths.scss %>/*.scss'],
        tasks: ['compass']
      }
    }
    //shell : {
      //runserver : {
      //  command : 'python manage.py runserver',
      //  options : {
      //    stdout: true,
      //    execOptions:{
      //      cwd : 'src'
      //    }
      //  }
      //},
      //activate : {
      //  command : 'source ../Scripts/activate'
        //options : {
          //execOptions:{
          //  cwd : '../Scripts'
          //}
        //}
      //}
    //}
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  //grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', ['jshint', 'concat', 'uglify', 'compass']);
  //grunt.registerTask('activate', ['shell:activate']);

};