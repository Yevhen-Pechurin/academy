odoo.define('rental.car', function(require) {
            'use strict';

            const FieldChar = require('web.basic_fields').FieldChar;

            const fieldRegistry = require('web.field_registry');
            const CustomFieldChar = FieldChar.extend({
                    events: _.extend({}, FieldChar.prototype.events, {
                        'input': '_onInput',
                    }),
                    init: function() {
                        this._super.apply(this, arguments);
                    },
                    _onInput: function() {
                        const self = this;
                        const query = this.$el.val()
                        this._rpc({
                            model: 'rental.car',
                            method: 'get_model',
                            args: [query],
                        }).then((data) => {
                            console.log(data)
                            //            console.log(data)
                        })
                    }
            })

            fieldRegistry.add('my-custom-field', CustomFieldChar);
            });
