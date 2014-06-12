(function(){
    var app = angular.module('messageCreate', []);
    app.controller('MsgCreateController', function($scope, $http){
        $scope.model = {};
        $scope.submit = function(){
            var data = {};
            data.field1 = $scope.model.field1;
            data.field2 = $scope.model.field2;
            data.author = $scope.model.author;

            $scope.model.isLoading = true;
            //TODO: POST Message Data

            $http.post('/create', data)
                .success(function(data, status, headers, config){
                    window.location = '#/message/' + data.uid;
                })
                .error(function(data, status, headers, config){
                    alert('Error: status - ' + status);
                    $scope.model.isLoading = false;
                });
        };
    });
})();
