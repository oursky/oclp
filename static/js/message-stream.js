(function(){
    var app = angular.module('messageStream', []);

    app.controller('MsgStreamController', function($scope, $routeParams, $http){
        $scope.model = {};
        $scope.model.page_id = $routeParams.page_id;
        $scope.model.result = [];

        $http.get('/stream?page=' + $scope.model.page_id)
            .success(function(data, status, headers, config){
                $scope.model.result = data.result;

                for (var i = $scope.model.result.length - 1; i >= 0; i--) {
                    $scope.model.result[i].datetime = new Date(Math.round($scope.model.result[i].uid / 1000));
                };

                console.log($scope.model.result);
            })
            .error(function(data, status){
                alert('Error: status - ' + status);
                window.location = "#/";
            });
    });
})();
