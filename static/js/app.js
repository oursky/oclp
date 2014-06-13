(function(){
    var app = angular.module('oclp', ['ngRoute', 'messageStream', 'messageCreate', 'messagePage']);
    app.config(function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $routeProvider
            .when('', {
                templateUrl: '/views/message-stream.html',
                controller: 'MsgStreamController'
            })
            .when('/', {
                templateUrl: '/views/message-stream.html',
                controller: 'MsgStreamController'
            })
            .when('/create', {
                templateUrl: '/views/message-create.html',
                controller: 'MsgCreateController'
            })
            .when('/message/:message_id', {
                templateUrl: '/views/message-page.html',
                controller: 'MsgPageController'
            })
            .otherwise({
                redirectTo: '/'
            });
    });
})();

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
                        window.location = '/message/' + data.uid;
                    }, 1000);
                })
                .error(function(data, status, headers){
                    alert('Error: status - ' + status);
                    $scope.model.isLoading = false;
                });
        };
    });
})();

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
                window.location = "/";
            });
    });
    
})();

(function(){
    var app = angular.module('messageStream', ['infinite-scroll']);

    app.controller('MsgStreamController', function($scope, $routeParams, $http){
        $scope.model = {};
        $scope.model.page_num = 0;
        $scope.model.result = [];
        $scope.model.isLoading = false;
        $scope.model.isLoadEnd = false;

        //set front page as height as viewport and color change
        $('#front-page').height($(window).height());

        $(window).scroll(function(){
            if($(window).scrollTop() > $(window).height() / 2){
                $('body').addClass('blue');
            }
            if($(window).scrollTop() < $(window).height() / 2){
                $('body').removeClass('blue');
            }
        });
        
        $scope.loadPage = function(pageNum){
            pageNum = pageNum || 1;

            $http.get('/stream?page=' + pageNum)
                .success(function(data, status, headers, config){
                    $scope.model.isLoading = false;

                    if(data.count == 0){
                        $scope.model.isLoadEnd = true;
                    }

                    for (var i = data.result.length - 1; i >= 0; i--) {
                        data.result[i].datetime = new Date(Math.round(data.result[i].uid / 1000));
                    }

                    $scope.model.result = $scope.model.result.concat(data.result);
                })
                .error(function(data, status){
                    alert('Error: status - ' + status);
                    window.location = "/";
                });
        };

        $scope.loadMore = function(){
            $scope.model.isLoading = true;
            $scope.model.page_num += 1;
            $scope.loadPage($scope.model.page_num);
        };
    });

    app.directive('whenScrolled', function() {
        return function(scope, elm, attr) {
            var raw = elm[0];
            
            elm.bind('scroll', function() {
                if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
                    scope.$apply(attr.whenScrolled);
                }
            });
        };
    });
})();
