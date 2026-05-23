# 🤖 Smart Job AI — Remote Accounting Job Hunter

Gecə-gündüz remote mühasibat işlərini axtarır, AI ilə analiz edir, Telegram-a göndərir.

## Qurulum

### 1. API Key-lər lazımdır

**Anthropic API Key:**
- console.anthropic.com → qeydiyyat → API Keys → Create Key
- Pulsuz $5 kredit verilir (başlanğıc üçün kifayətdir)

**Telegram Bot Token:**
- Artıq var: BotFather-dən aldığın token

### 2. Railway-də Deploy et (pulsuz)

1. github.com → yeni repo yarat → bu faylları upload et
2. railway.app → "Deploy from GitHub" → repo-nu seç
3. Variables bölməsində bunları əlavə et:

```
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=1523955514
ANTHROPIC_API_KEY=your_key
CHECK_INTERVAL_MINUTES=30
```

4. Deploy → proqram işə düşür!

### 3. Lokal test (istəsən)

```bash
pip install -r requirements.txt
cp .env.example .env
# .env faylını öz məlumatlarınla doldur
python main.py
```

## Platformalar

- Jobicy.com (remote accounting)
- WeWorkRemotely (finance jobs)
- RemoteOK (accounting)
- Indeed (bookkeeper remote)
- Jobspresso

## Necə işləyir

1. Hər 30 dəqiqədə bütün feed-ləri yoxlayır
2. Açar sözlərə görə filtr edir
3. Claude AI ilə hər elanı analiz edir (skor 0-100)
4. Skor 50+ olan işləri Telegram-a göndərir
5. Hazır proposal (cover letter) da göndərir
6. Artıq görülmüş elanları yaddaşda saxlayır (dublikat yoxdur)
