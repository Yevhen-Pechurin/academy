odoo.define('rental.car', function(require) {
            'use strict';
            const core = require('web.core');
            const QWeb = core.qweb;

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
                            this.data_model = data
                            if (data && data.length > 0) {
                                const elem = $(QWeb.render('rental.model_list', {
                                    list_search: data,
                                    }));
                                elem.find('.list_car_span').on('click', self._onClickModel.bind(self));
//                                self.$el.after(elem);
                                self.appendTo("body");
                                }
                            //            console.log(data)
                        })
                    },
                    _onClickModel: function(self) {
                    console.log(this.data_model)
                }
            })

            fieldRegistry.add('my-custom-field', CustomFieldChar);
            });
