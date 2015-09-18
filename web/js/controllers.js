
var atrapControllers = angular.module('atrapControllers', []);

atrapControllers.controller('LiveOverviewCtrl', ['$scope', 'AllPlayerIDs', 'Player',
  function($scope, AllPlayers, Player) {
    $scope.playerData = {};
    $scope.playerIDs = AllPlayers.get(function (player_list) {
      for (var i = 0; i < player_list.all_players.length; i++) {
        var id_a = parseInt(player_list.all_players[i]);
        $scope.playerData[id_a] = Player.get({playerID: id_a}, function(player) {
          $scope.playerData[id_a] = player;
        });
      }
    });

  }]);

atrapControllers.controller('PlayerDetailsCtrl', ['$scope', '$routeParams', 'Player',
  function($scope, $routeParams, Player) {
    $scope.player = Player.get({playerID: $routeParams.playerID});
  }]);
