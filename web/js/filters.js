
var atrapFilters = angular.module('atrapFilters', []);

atrapFilters.filter('num', function() {
  return function(input) {
    return parseInt(input);
  };
});
