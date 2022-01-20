odoo.define('rental.test', function(require) {
    'use strict';

    const FieldChar = require('web.basic_fields').FieldChar;

    const CustomFieldChar = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
        }),
        init: function() {
            this._super.apply(this, arguments); //this._super();
        },
        _onInput: function() {
            const self = this;
            const query = this.$el.val()
            this._rpc({
                model: 'rental.car',
                method: 'get_model',
                args: [query],
            }).then((data) => {
                console.log(data);
            })
        }

    });

    const fieldRegistry = require('web.field_registry');

    fieldRegistry.add('my-custom-field', CustomFieldChar);

    //<field name="model" widget="my-custom-field"/>

});


/* var basic_fields = require('web.basic_fields');
var Phone = basic_fields.FieldPhone;

Phone.include({
    events: _.extend({}, Phone.prototype.events, {
        'click': '_onClick',
    }),

    _onClick: function (e) {
        if (this.mode === 'readonly') {
            e.preventDefault();
            var phoneNumber = this.value;
            // call the number on voip...
        }
    },
}); */