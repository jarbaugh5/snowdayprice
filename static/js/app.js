'use strict';

var snowApp = angular.module('snowApp', ['autocomplete']);

snowApp.controller('SnowAppCtrl', function ($scope, $filter) {
    $scope.schoolDict = {
        'Tufts': 'a',
        'Harvard': 'a',
        'MIT': 'a',
        'UMass Boston': 'a'
    };

    $scope.newSchoolList = [];

    $scope.selectedSchool = '';

    $scope.updateSchools = function (typed) {
        $scope.newSchoolList = $filter('filter')(Object.keys($scope.schoolDict), typed);
    };

    $scope.selectSchool = function (schoolName) {
        if ($scope.schoolDict[schoolName]) {
            console.log('School detected: ' + schoolName);
        }
    };
});