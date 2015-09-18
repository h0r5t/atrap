var atrapServices = angular.module('atrapServices', ['ngResource']);

atrapServices.factory('Player', ['$resource',
  function($resource){
    return $resource('live/players/:playerID.json', {});
  }]);

atrapServices.factory('AllPlayerIDs', ['$resource',
  function($resource){
    return $resource('live/player_list.json', {});
  }]);
