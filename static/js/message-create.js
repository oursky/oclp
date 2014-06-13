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

            $http.post('/create', data)
                .success(function(data, status, headers){
                    setTimeout(function(){
                        window.location = '#/message/' + data.uid;
                    }, 1000);
                })
                .error(function(data, status, headers){
                    alert('Error: status - ' + status);
                    $scope.model.isLoading = false;
                });
        };
    });
})();
