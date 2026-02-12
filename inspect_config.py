from causica.training.auglag import AugLagLRConfig
try:
    config = AugLagLRConfig()
    print("Keys in lr_init_dict:", config.lr_init_dict.keys())
    print("Full dict:", config.lr_init_dict)
except Exception as e:
    print(e)
