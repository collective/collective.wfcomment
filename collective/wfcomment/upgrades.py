def upgrade_2_3(context):
    context.runImportStepFromProfile('profile-collective.wfcomment:default',
                                     'kssregistry', run_dependencies=False,
                                     purge_old=False)