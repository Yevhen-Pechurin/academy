odoo.define('zoom_info.zoom_list', function (require) {
    'use strict';
    const core = require('web.core');
    const QWeb = core.qweb;

    const field_registry = require('web.field_registry');
    const basic_fields = require('web.basic_fields');
    const FieldChar = basic_fields.FieldChar;
    const framework = require('web.framework');
    const {
        findCompanyId,
        findCompanyInfo,
        findContactByName,
        findContactByPosition,
        findContactInfo,
    } = require('zoom_info.zoom_info_query');

    const createListCompany = (self, data) => {
        self.$el.parent().find('.zoom_search_div').remove();
        if (data.length > 0) {
            const elem = $(QWeb.render('zoom_info.zoom_list', {
                list_search: data,
            }));
            elem.find('.list_person_span').on('click', self._onClickCompany.bind(self));
            self.$el.after(elem);
        }
        framework.unblockUI()
    }

    const createListPerson = (self, data) => {
        if (data.length > 0) {
            self.$el.parent().find('.zoom_contact_div').remove();
            const elem = $(QWeb.render('zoom_info.zoom_list_contact', {
                list_contact: data,
            }));
            elem.find('.list_contact_div').on('click', self._onClickContact.bind(self));
            self.$el.focusout(function () {
                setTimeout(() => {
                    self.$el.parent().find('.zoom_contact_div').remove();
                }, 200);
            });
            self.$el.after(elem);
        } else {
            self.$el.parent().find('.zoom_contact_div').remove();
        }
        framework.unblockUI()
    }

    const FieldAutocompleteZoomAPI = FieldChar.extend({
        className: 'o_field_partner_zoom_info',
        events: _.extend({}, FieldChar.prototype.events, {
            'input': '_onInput',
            'keyup': '_onKeyUp',
        }),
        start: function () {
            this._super.apply(this, arguments);
            this._timeout = 0;
        },

        _onInput: function (e) {
            const type = this._typeField(e);
            if (!type) {
                return;
            }

            if (this._timeout) {
                clearTimeout(this._timeout);
            }

            let self = this;
            const query = this.$el.val();
            const re = new RegExp(/^[A-Za-z -._]+$/);

            if (!re.test(query)) {
                self.$el.parent().find('.zoom_search_div').remove();
                return;
            }
            self.$el.parent().css('position', 'relative')

            this._timeout = setTimeout(() => {
                if (type === 'company') {
                    this._findCompanyAndRender(self, query);
                }
                if (type === 'contact') {
                    this._findContactAndRender(self, query);
                }
            }, 500);

        },

        _findCompanyAndRender: function (self, query) {
            framework.blockUI();
            findCompanyId(self, query).then(data => {
                createListCompany(self, data);
            });
        },

        _findContactAndRender: function (self, query) {
            framework.blockUI()
            const companyId = $('h1 input[name="zoom_api_company_id"]').val();

            if (!companyId) {
                return;
            }

            if (self.$el[0].name === 'name') {
                findContactByName(self, query, companyId).then(data => {
                    createListPerson(self, data);
                })
            }
            if (self.$el[0].name === 'function') {
                findContactByPosition(self, query, companyId).then(data => {
                    createListPerson(self, data);
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
            framework.blockUI()
            this._insertCompanyData(e.target.dataset.id);
        },

        _onClickContact: function (e) {
             framework.blockUI()
            this._insertPersonData(e.currentTarget.dataset.id);
        },

        _insertCompanyData: function (companyId) {
            const self = this;
            findCompanyInfo(self, companyId).then(res => {
                if (res.length === 0) {
                    self.$el.parent().find('.zoom_search_div').remove();
                    return;
                }
                const data = res;
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

                changes = {
                    'name': name,
                    'street': street,
                    'city': city,
                    'zip': zipCode,
                    'phone': phone,
                    'website': website,
                    'zoom_api_company_id': companyId,
                    'country_id': {id: country},
                    'state_id': {id: state},
                    'image_1920': logo,
                }

                $name.val(name);

                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    operation: 'UPDATE',
                    changes: changes
                })

                self.$el.parent().find('.zoom_search_div').remove();
                framework.unblockUI()
            })
        },

        _insertPersonData: function (personId) {
            const self = this;
            findContactInfo(self, personId).then(res => {
                if (res.length === 0) {
                    self.$el.closest('table').find('.zoom_contact_div').remove();
                    return;
                }
                const data = res;
                const name = data.firstName + ' ' + data.lastName;
                const jobTitle = data.jobTitle;
                const phone = data.phone;
                const email = data.email;
                const pictureUrl = data.picture;

                self.$el.closest('table').find('.zoom_contact_div').remove();
                self.el.name === 'function' ? self.$el.val(jobTitle) : self.$el.val(name);

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
                framework.unblockUI()
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
