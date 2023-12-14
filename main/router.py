dcp_models = ['bpcsech', 'bpcsechsettings', 'bpcsecl', 'bpcsexport', 'bpcsmmexport', 'bpcsmmexportdetails',
              'bpcsmmexportsettings', 'aaaa', 'authgroup', 'authgrouppermissions', 'authpermission', 'authuser',
              'authusergroups', 'authuseruserpermissions', 'box', 'config', 'connection', 'djangoAdminLog',
              'djangocontenttype', 'djangomigrations', 'djangosession', 'packaging', 'pallet', 'pattern',
              'productsdata', 'role', 'rwreason', 'scans', 'session', 'sysdiagrams', 'tbommaterials', 'tbomproducts',
              'tboms', 'tboxlabelcounter', 'tcardboardstockmovements', 'tcardboardstocks', 'tcompany', 'tcontainer',
              'tcontainerhistory', 'tcontainerwashing', 'tcontracts', 'tcountryoforigin', 'tcurrency', 'tcustomers',
              'tdailyinventory', 'tdailyinventoryconfirmations', 'tdashboardminstock', 'tdelivery',
              'tdeliveryratingparams', 'tdeliveryratings', 'tdeliverystatus', 'tinvboxstatus', 'tinvheader',
              'tinvvolume', 'tkioskmessage', 'tlocations', 'tlocationscontent', 'tmovecode', 'tmovementhistory',
              'torderstatus', 'tordersdetail', 'tordersheader', 'tpalletinbound', 'tprodcustcode', 'tprodlines',
              'tproductionordercontainers', 'tproductionordercontainersreturns', 'tproductionorders',
              'treportrawmaterialpartsbo', 'treportrawmaterialpartsmonths', 'treportrawmaterialpartsqty',
              'treportrawmaterialpartswatch', 'tsalesorders', 'tsalesordersdetails', 'tsalesordersstatus', 'tsettings',
              'tshipmentdetails', 'tshipped', 'tsupplier', 'ttradeterms', 'tunits', 'twashingstations', 'tweight',
              'testweight', 'unscannedserials', 'users', 'warehousevolume', 'warehouses']
barcodes_models = ['rawpacking', 'settings', 'production', 'productiondev', 'tmachineauto','tproductiontmp',
                   'tverification', 'tvisionpictureconfigs']

class DBRouter:

    def db_for_read(self, model, **hints):
        if model._meta.model_name in barcodes_models:
            print('READ bc')
            return 'barcodes'
        elif model._meta.model_name in dcp_models:
            print('READ dcp')
            return 'dcp'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.model_name in barcodes_models:
            print('WRITE_BC')
            return 'barcodes'
        elif model._meta.model_name in dcp_models:
            print('WRITE_DCP')
            return 'dcp'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name in barcodes_models or obj2._meta.model_name in barcodes_models:
            return True
        elif obj1._meta.model_name not in [barcodes_models, dcp_models]:
            return True
        elif obj1._meta.model_name in dcp_models or obj2._meta.model_name in dcp_models:
            return True
        elif obj2._meta.model_name not in [barcodes_models, dcp_models]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in barcodes_models:
            print('MIGRATE bc')
            return db == 'barcodes'
        if model_name in dcp_models:
            print('MIGRATE dcp')
            return db == 'dcp'
        return None

