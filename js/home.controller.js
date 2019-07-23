angular.module("blogApp", [])
.controller("HomePageController", homePageController)
.service("DataGetService", dataGetService);
homePageController.$inject = ['$scope', 'DataGetService']
function homePageController($scope, DataGetService) {
    var ctrl = this;

    ctrl.articleList = [];
    ctrl.init = init;

    function init() {
        DataGetService.getAll()
            .then(function(response) {
                console.log(response);
                ctrl.articleList = response;
            }, function(error) {
                console.err(error);
                alert("Some error occurred.");
            })
    }
}

dataGetService.$inject = ['$http']
function dataGetService($http) {
    return {
        getAll: getAll
    }

    function getAll() {
        return $http.get(url: '/get_all_posts')
    }
}
