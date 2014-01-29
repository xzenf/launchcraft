VERSION = '1.7.2'

MODS = {
    'optifine': {
        'name': 'Optifine',
        'version': '1.7.2_HD_U_C2',
        'url': 'http://optifine.net/download.php?f=OptiFine_1.7.2_HD_U_C2.jar',
        'deps': {}
    },
    'reis': {
        'name': 'REI\'s Minimap',
        'version': '3.4_03beta',
        'url': 'https://dl.dropboxusercontent.com/u/34787499/minecraft/1.7.2/%5B1.7.2%5DReiMinimap_v3.4_03beta.zip',
        'deps': {}
    },
    'status_effect_hud': {
        'name': 'Status Effect HUD',
        'version': '1.21',
        'url': 'http://dl.dropboxusercontent.com/u/20748481/MC/StatusEffectHUD/latest/%5B1.7.2%5DStatusEffectHUD-client-1.21(1.7.2).jar',
        'deps': {'forge', 'bspkrsCore'}
    },
    'armor_status_hud': {
        'name': 'Armor Status HUD',
        'version': '1.18',
        'url': 'http://dl.dropboxusercontent.com/u/20748481/MC/ArmorStatusHUD/latest/%5B1.7.2%5DArmorStatusHUD-client-1.18(1.7.2).jar',
        'deps': {'forge', 'bspkrsCore'}
    },
    'bspkrsCore': {
        'name': 'bspkrsCore',
        'version': '6.0',
        'url': 'http://bspk.rs/MC/bspkrsCore/%5B1.7.2%5DbspkrsCore-universal-6.0(1.7.2).jar',
        'deps': {'forge'}
    },
    'forge': {
        'name': 'Forge',
        'version': '10.12.0.1021',
        'url': 'http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.7.2-10.12.0.1021/forge-1.7.2-10.12.0.1021-installer.jar',
        'deps': {}
    }
}
