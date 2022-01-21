odoo.define('rental.test', function(require) {
    'use strict';

    const core = require('web.core');
    const Qweb = core.qweb;
    const FieldChar = require('web.basic_fields').FieldChar;

    const CustomFieldChar = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
            'focusout': '_onFocusoutCleanup',
        }),
        init: function() {
            this._super.apply(this, arguments); //this._super(...arguments);
        },
        _onFocusoutCleanup: function() {
            setTimeout(() => {
                this.$el.parent().find('.test_search_div').remove();
            }, 100);
            
        },
        _onClickGetModelInfo: function(e) {
            const self = this;
            this._rpc({
                model: 'rental.car_model',
                method: 'read',
                args: [[+e.target.dataset.id], ['model_name', 'manufacturer_logo']],
            }).then((res) => {
                console.log(res);

                const info = {
                    model: res[0].model_name || '',
                    logo: res[0].manufacturer_logo || '',
                }

                self.$el.val(res[0].model_name);
                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: info,
                })

                self.$el.parent().find('.test_search_div').remove();
                e.stopPropagation();
            })
        },
        _onClickRenderTemplate: function(self, data) {
            self.$el.parent().find('.test_search_div').remove();
            if (data.models && data.models.length > 0) {
                const elem = $(Qweb.render('test_template', {
                    list_search: data.models,
                }));
                elem.find('.list_car_model').on('click', self._onClickGetModelInfo.bind(self));
                self.$el.after(elem);
            }
        },
        _onInput: function() {
            const self = this;
            const query = this.$el.val()
            this._rpc({
                model: 'rental.car',
                method: 'get_model',
                args: [query],
            }).then((res) => {
                this._onClickRenderTemplate(self, res);
            })
        }

    });

    const fieldRegistry = require('web.field_registry');

    fieldRegistry.add('my-custom-field', CustomFieldChar);

});