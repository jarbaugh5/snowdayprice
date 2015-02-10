'use strict';

var snowApp = angular.module('snowApp', ['autocomplete']);

snowApp.service('GetData', function ($http) {
    return {
        'getSchoolData': function (cb) {
            $http.get('static/json/college_data.json')
                .success(function(data) {
                    console.log(data);
                    cb(data);
                })
                .error(function(data) {
                    console.log('Error getting data.');
                });
        }
    };
});

snowApp.controller('SnowAppCtrl', function ($scope, $filter, GetData) {
    $scope.schoolDict = {};

    GetData.getSchoolData(function (data) {
        $scope.schoolDict = data;
    });

    $scope.newSchoolList = [];

    $scope.selectedSchool = '';

    $scope.updateSchools = function (typed) {
        $scope.newSchoolList = $filter('filter')(Object.keys($scope.schoolDict), typed);
    };

   $scope.isPositiveInteger = function (n) {
        return 0 === n % (!isNaN(parseFloat(n)) && 0 <= ~~n);
    }

    $scope.selectSchool = function (schoolName) {
        if ($scope.schoolDict[schoolName]) {
            $scope.selectedSchool = $scope.schoolDict[schoolName];
            console.log('School detected: ' + schoolName);
        }
    };
});