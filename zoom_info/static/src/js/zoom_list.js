odoo.define('zoom_info.zoom_list', function (require) {
    'use strict';
    const core = require('web.core');
    const QWeb = core.qweb;

    const field_registry = require('web.field_registry');
    const basic_fields = require('web.basic_fields');
    const FieldChar = basic_fields.FieldChar;

    const FieldAutocompleteZoomAPI = FieldChar.extend({
        className: 'o_field_partner_zoom_info',
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
            'keyup': '_onKeyUp',
        }),
        start:function () {
            this._super.apply(this, arguments);
            this._timeout = 0;
        },

        _onInput: function (e) {
            const type = this._typeField(e);
            if (!type) {
                return;
            }

            let self = this;
            const query = this.$el.val();
            self.$el.parent().css('position', 'relative')
            if (!query) {
                self.$el.parent().find('.zoom_search_div').remove();
                return;
            }

            if (this._timeout){
                clearTimeout(this._timeout);
            }


            this._timeout = setTimeout(() => {
                if (type === 'company') {
                    this._findCreateCompany(self, query);
                }
                if (type === 'contact') {
                    this._findCreateContact(self, query);
                }
            }, 500);

        },

        _findCreateCompany: function (self, query) {
            self._rpc({
                model: 'res.config.settings',
                method: 'zoom_info_request',
                args: ['search/company'],
                kwargs: {
                    uri: 'search/company',
                    params: {
                        "companyName": query
                    }
                },
            }).then(res => {
                self.$el.parent().find('.zoom_search_div').remove();
                if (res.data && res.data.length > 0) {
                    const elem = $(QWeb.render('zoom_info.zoom_list', {
                        list_search: res.data,
                    }));
                    elem.find('.list_person_span').on('click', this._onClickCompany.bind(this));
                    self.$el.after(elem);
                }
            })
        },

        _findCreateContact: function (self, query) {
            const companyId = $('h1 input[name="zoom_api_company_id"]').val();

            if (!companyId) {
                return;
            }

            if (self.$el[0].name === 'name') {
                self._rpc({
                    model: 'res.config.settings',
                    method: 'zoom_info_request',
                    args: ['search/contact'],
                    kwargs: {
                        uri: 'search/contact',
                        params: {
                            "fullName": query,
                            "companyId": companyId,
                        },
                    },
                }).then(res => {
                    if (res.data.length > 0) {
                        self.$el.parent().find('.zoom_contact_div').remove();
                        const elem = $(QWeb.render('zoom_info.zoom_list_contact', {
                            list_contact: res.data,
                        }));
                        elem.find('.list_contact_div').on('click', this._onClickContact.bind(this));
                        self.$el.focusout(function () {
                            setTimeout(() => {
                                self.$el.parent().find('.zoom_contact_div').remove();
                            }, 200);
                        });
                        self.$el.after(elem);
                    } else {
                        self.$el.parent().find('.zoom_contact_div').remove();
                    }
                })
            }
            if (self.$el[0].name === 'function') {
                self._rpc({
                    model: 'res.config.settings',
                    method: 'zoom_info_request',
                    args: ['search/contact'],
                    kwargs: {
                        uri: 'search/contact',
                        params: {
                            "jobTitle": query,
                            "companyId": companyId,
                        },
                    },
                }).then(res => {
                    if (res.data.length > 0) {
                        self.$el.parent().find('.zoom_contact_div').remove();
                        const elem = $(QWeb.render('zoom_info.zoom_list_contact', {
                            list_contact: res.data,
                        }));
                        elem.find('.list_contact_div').on('click', this._onClickContact.bind(this));
                        self.$el.focusout(function () {
                            setTimeout(() => {
                                self.$el.parent().find('.zoom_contact_div').remove();
                            }, 200);
                        });
                        self.$el.after(elem);
                    } else {
                        self.$el.parent().find('.zoom_contact_div').remove();
                    }
                })
            }
        },

        _typeField: function (e) {
            const company = $(e.currentTarget).closest('.oe_title').find('div[name="company_type"] input:checked').data('value');
            if (company === 'company') {
                return 'company';
            }
            const contact = $(e.currentTarget).closest('.o_form_sheet').find('input:checked').data('value');
            if (contact === 'contact') {
                return 'contact';
            }
            return '';
        },

        _onClickCompany: function (e) {
            this._findAndInsertCompany(e.target.dataset.id);
        },

        _onClickContact: function (e) {
            this._findAndInsertContact(e.currentTarget.dataset.id);
        },

        _findAndInsertCompany: function (id) {
            const self = this;
            this._rpc({
                model: 'res.config.settings',
                method: 'zoom_info_request',
                args: ['enrich/company'],
                kwargs: {
                    uri: 'enrich/company',
                    params: {
                        "matchCompanyInput": [{"companyId": id}],
                        "outputFields": [
                            "name",
                            "street",
                            "city",
                            "state",
                            "zipCode",
                            "country",
                            "phone",
                            "website",
                            "logo",
                        ]
                    }
                },
            }).then(res => {
                if (res.success) {
                    const data = res.data.result[0].data[0];
                    const name = data.name || "";
                    const street = data.street || "";
                    const city = data.city || "";
                    const state = data.state || "";
                    const zipCode = data.zipCode || "";
                    const country = data.country || "";
                    const phone = data.phone || "";
                    const website = data.website || "";
                    const logo = data.logo || "";

                    const $parent = self.$el.closest('.o_form_sheet_bg');

                    const $name = $parent.find('input[name="name"]');

                    let changes = {};

                    self._rpc({
                        model: 'res.partner',
                        method: 'get_country',
                        args: [],
                        kwargs: {
                            country_name: country,
                            state_name: state,
                        },
                    }).then(res => {
                        changes = {
                            'name': name,
                            'street': street,
                            'city': city,
                            'zip': zipCode,
                            'phone': phone,
                            'website': website,
                            'zoom_api_company_id': id,
                            'country_id': {id: res.country_id},
                            'state_id': {id: res.state_id},
                            'image_1920': logo,
                        }

                        $name.val(name);

                        self.trigger_up('field_changed', {
                            dataPointID: self.dataPointID,
                            operation: 'UPDATE',
                            changes: changes
                        })

                        self.$el.parent().find('.zoom_search_div').remove();
                    })
                }
            });
        },

        _findAndInsertContact: function (id) {
            const self = this;
            this._rpc({
                model: 'res.config.settings',
                method: 'zoom_info_request',
                args: ['enrich/contact'],
                kwargs: {
                    uri: 'enrich/contact',
                    params: {
                        "matchPersonInput": [{"personId": id}],
                        "outputFields": [
                            "firstName",
                            "lastName",
                            "email",
                            "phone",
                            "jobTitle",
                            "picture",
                        ]
                    },
                },
            }).then(res => {
                const data = res.data.result[0].data[0];
                const name = data.firstName + ' ' + data.lastName;
                const jobTitle = data.jobTitle;
                const phone = data.phone;
                const email = data.email;
                const pictureUrl = data.picture;

                self.$el.closest('table').find('.zoom_contact_div').remove();

                self.$el.val(name);

                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: {
                        name: name,
                        function: jobTitle,
                        phone: phone,
                        email: email,
                        image_1920: pictureUrl
                    },
                });
            });
        },

        _onKeyUp: function (ev) {
            ev.preventDefault()
            if (ev.keyCode === $.ui.keyCode.ESCAPE) {
                this.$el.parent().find('.zoom_search_div').remove()
            }
        }
    });


    field_registry.add('field_partner_zoom_info', FieldAutocompleteZoomAPI);
    return FieldAutocompleteZoomAPI;

});
