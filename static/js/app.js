(function(){
    var app = angular.module('oclp', ['ngRoute', 'messageStream', 'messageCreate', 'messagePage']);
    app.config(function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl: 'views/front-page.html'
            })
            .when('/stream', {
                redirectTo: '/stream/1'
            })
            .when('/stream/:page_id', {
                templateUrl: 'views/message-stream.html',
                controller: 'MsgStreamController'
            })
            .when('/create', {
                templateUrl: 'views/message-create.html',
                controller: 'MsgCreateController'
            })
            .when('/message/:message_id', {
                templateUrl: 'views/message-page.html',
                controller: 'MsgPageController'
            })
            .otherwise({
                redirectTo: '/'
            });
    });
})();
