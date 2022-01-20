odoo.define('rental_car.car_widget', function (require) {
    'use strict';

    const Widget = require('web.Widget');
    const FieldChar = require('web.basic_fields').FieldChar;
    const fieldRegistry = require('web.field_registry');

    const CustomFieldChar = FieldChar.extend({
        className: 'o_field_partner_rental_car',

        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
        }),

        init: function () {
            this._super.apply(this, arguments);
            console.log('My Test Field - 222');
            this.data = [];
        },

        _onInput: function () {
            console.log(this.$el.val());
        }
    });

    fieldRegistry.add('my_custom_field', CustomFieldChar);

    // return {CustomFieldChar, Widget}
})

