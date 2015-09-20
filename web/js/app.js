
var atrapApp = angular.module('atrapApp', [
  'ngRoute',
  'atrapFilters',
  'atrapControllers',
  'atrapServices'
]);

atrapApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/live', {
        templateUrl: 'partials/live-overview.html',
        controller: 'LiveOverviewCtrl'
      }).
      when('/live/players/:playerID', {
        templateUrl: 'partials/player-details.html',
        controller: 'PlayerDetailsCtrl'
      }).
      otherwise({
        redirectTo: '/live'
      });
  }]);
