odoo.define('rental.car', function (require) {
    'use strict';
    const Widget = require("web.Widget");
    const FieldChar = require('web.basic_fields').FieldChar;
    const fieldRegistry = require('web.field_registry');


    const CustomFieldChar = FieldChar.extend({
        init: function () {
            this._super.apply(this, arguments);
            console.log('TEST');
        },
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput'
        }),
        _onInput:function () {
            console.log(this.$el.val());
        }
    });


    fieldRegistry.add('list_field', CustomFieldChar);
})
