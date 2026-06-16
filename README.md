# Otonom Elektrikli Hastane Servis Robotu - İP1 SLAM

Bu ROS 2 (Humble) paketi, hastane koridorları gibi yüksek dinamikli alanlar için optimize edilmiş Google Cartographer ve EKF (Genişletilmiş Kalman Filtresi) tabanlı SLAM mimarisini içermektedir. Rapor kapsamında belirtilen `r=0.05m` çözünürlük optimizasyonları ve alt-harita (submap) bellek ayarları entegre edilmiştir.

## Kurulum ve Test (Test Instructions)
Test ortamında bu paketi derlemek ve çalıştırmak için aşağıdaki ROS 2 terminal komutlarını sırasıyla uygulayınız.

**1. Çalışma Alanını (Workspace) Oluşturma ve Klonlama:**
```bash
mkdir -p ~/hospital_ws/src
cd ~/hospital_ws/src
git clone [https://github.com/elifover/Hospital-Robot-SLAM-Nav2.git](https://github.com/elifover/Hospital-Robot-SLAM-Nav2.git)
