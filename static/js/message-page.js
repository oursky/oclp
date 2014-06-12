(function(){
    var app = angular.module('messagePage', []);
    app.controller('MsgPageController', function($scope, $routeParams){
        $scope.model = {};
        $scope.model.message_id = $routeParams.message_id;
    });
    
})();
