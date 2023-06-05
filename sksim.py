#Author Hamayon khan
import subprocess
try:
    sim_id = ''
    android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
    model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
    build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
    fblc = 'en_GB'
    try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
    except:
        fbcr = 'Zong'
    fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
    fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
    fbdv = model
    fbsv = android_version
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
    fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
    try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
            total+=1
        select = ('1','2')
        if select == '1':
            fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
            sim_id+=fbcr
        elif select == '2':
            try:
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                sim_id+=fbcr
            except Exception as e:
                fbcr = "Zong"
                sim_id+=fbcr
        else:
            fbcr = 'Zong'
            sim_id+=fbcr
    except:
        fbcr = "Zong"
    device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
    print("device = ", device)
    print("sim id = ", sim_id)
except Exception as e:
    print("An error occurred: ", str(e))
    
    [FBAN/FB4A;FBAV/;FBBV/;[FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]
