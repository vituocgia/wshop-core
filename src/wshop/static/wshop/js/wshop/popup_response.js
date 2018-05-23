/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('wshop-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.wshop.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.wshop.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.wshop.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();
