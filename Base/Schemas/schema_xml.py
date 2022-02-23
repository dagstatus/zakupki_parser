class Schema:
    # Тут поля и названия которые могут меняться в зависимости от версий
    schema_time = {
        'supplier': ['suppliers', 'suppliersInfo'],
        'customer': ['customer', 'customer'],
        'finances': ['finances'],
        'printForm': ['printForm'],
        'currentContractStage': ['currentContractStage'],
        'contractSubject' : ['contractSubject'],
        'id': ['id']
    }
    # а тут поля и если данные вложены то указываем какие поля вытащить, если нет вложенных то пустой массив
    need_vars = {
        'customer': ['inn', 'kpp', 'fullName', 'shortName'],
        'supplier': ['inn', 'kpp', 'fullName', 'shortName', 'address'],
        'finances': ['paymentSumRUR', 'startDate', 'endDate', 'paymentSumRUR'],
        'printForm': ['url'],
        'currentContractStage': [],
        'contractSubject': [],
        'id': []
    }
