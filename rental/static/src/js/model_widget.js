odoo.define('rental.model_widget', function (require) {
    'use strict';
    const Widget = require('web.Widget');

    var FieldChar = require('web.basic_fields').FieldChar;
    var FieldRegistry = require('web.field_registry');

    var CustomFieldChar = FieldChar.extend({
        className: 'o_field_partner_rental',

        // xmlDependencies: ['/rental/static/src/xml/model_widget.xml'],
        template: 'rental.rental_template',

        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
        }),
        init: function () {
            this._super.apply(this, arguments);
            console.log('TEST WORK');
            this.data = [];
        },

        _onInput: function () {
            console.log(this.$el.val());
            // this._rpc({
            //     model: 'res.partner',
            //     method: 'get_country',
            //     args: ['1', "1"],
            // });
        }

    });

    FieldRegistry.add('my_custom_field', CustomFieldChar);
})


