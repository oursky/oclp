(function(){
    var app = angular.module('messageStream', []);
    app.controller('MsgStreamController', function($scope, $routeParams){
        $scope.model = {};
        $scope.model.page_id = $routeParams.page_id;
    });
})();
