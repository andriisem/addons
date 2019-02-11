odoo.define('first_weekday.datepicker', function (require) {
"use strict";

    var datepicker = require('web.datepicker');

    datepicker.DateWidget.include({
        init: function (parent, options) {
            this._super(parent, _.extend({
                locale : moment.locale()
            }, options || {}));
        }
    });
});


