(function(){
    var app = angular.module('messagePage', []);
    app.controller('MsgPageController', function($scope, $routeParams, $http){
        $scope.model = {};
        $scope.model.message_id = $routeParams.message_id;

        $http.get('/message?id=' + $scope.model.message_id)
            .success(function(data, status, headers, config){

                $scope.model.field1 = data.field1;
                $scope.model.field2 = data.field2;
                $scope.model.author = data.author;
                $scope.model.datetime = new Date(Math.round($scope.model.message_id / 1000));

            })
            .error(function(data, status, headers, config){
                alert('Error: status - ' + status);
                window.location = "#/";
            });
    });
    
})();
