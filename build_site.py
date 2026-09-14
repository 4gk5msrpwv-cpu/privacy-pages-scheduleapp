#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ScheduleApp 隐私政策 / 支持页生成器（CloudKit 架构版）
与 KidLearn 的 privacy-pages 方案同构：
- 站点结构：根目录 = 英文版（ASC「隐私政策网址」必须填审核员可读的英文）；
  各语言位于 /{lang}/ 子目录，未覆盖语种回落英文。
- 语言：en（根）+ zh-Hans / zh-Hant / ja / es / pt-BR / fr / de / ko / ru（与 App 内 10 语一致）。
- 内容对应 CloudKit 去 ECS 架构：无账号体系、数据存用户自己的 iCloud、无第三方 SDK。
用法：python3 build_site.py  （输出到本目录各语言子文件夹）
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
EFFECTIVE = "2026-09-14"
DEV = "Frank Zhou"
MAIL = "your.scheduleapp@outlook.com"
LANGS = ["en", "zh-Hans", "zh-Hant", "ja", "es", "pt-BR", "fr", "de", "ko", "ru"]
NATIVE = {"en": "English", "zh-Hans": "简体中文", "zh-Hant": "繁體中文", "ja": "日本語",
          "es": "Español", "pt-BR": "Português (BR)", "fr": "Français", "de": "Deutsch",
          "ko": "한국어", "ru": "Русский"}

CSS = """<style>
:root{color-scheme:light dark;--bg:#ffffff;--fg:#1c1c1e;--fg2:#8a8a8e;--border:#d1d1d6;--quote:#f2f2f7;--accent:#0a84ff}
@media (prefers-color-scheme:dark){:root{--bg:#000000;--fg:#f2f2f7;--fg2:#98989f;--border:#38383a;--quote:#1c1c1e;--accent:#0a84ff}}
body{font-family:-apple-system,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:var(--fg);background:var(--bg);line-height:1.75;margin:0;padding:24px 16px;font-size:15px}
.wrap{max-width:760px;margin:0 auto}
h1{font-size:24px;margin:0 0 6px}
h2{font-size:18px;margin:28px 0 8px;border-left:4px solid var(--accent);padding-left:10px}
h3{font-size:15px;margin:14px 0 4px}
p,li{margin:7px 0}
.meta,.langs,.footer{color:var(--fg2);font-size:13px}
.langs{margin:10px 0 0}
.langs a{color:var(--accent);text-decoration:none;margin-right:2px}
blockquote{background:var(--quote);border-left:4px solid var(--fg2);margin:14px 0;padding:10px 14px;border-radius:6px}
a{color:var(--accent)}
.footer{margin-top:36px;border-top:1px solid var(--border);padding-top:12px}
</style>"""


def page(L):
    return f"""<!DOCTYPE html>
<html lang="{L['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="{L['desc']}">
<title>{L['title']}</title>
{CSS}
</head>
<body>
<div class="wrap">
<h1>{L['h1']}</h1>
<p class="meta">{L['meta_line']}</p>
<p class="langs">{L['lang_label']} {' · '.join(('<a href="/privacy-pages-scheduleapp/">' if lg=='en' else f'<a href="/privacy-pages-scheduleapp/{lg}/">')+NATIVE[lg]+'</a>' for lg in LANGS)}</p>
<blockquote><b>{L['in_short_label']}</b> {L['summary']}</blockquote>

<h2 id="privacy">{L['nav_privacy']}</h2>
{L['sections']}

<h2 id="faq">{L['nav_faq']}</h2>
{L['faq']}

<div class="footer">{L['footer']}</div>
</div>
</body>
</html>
"""


def ul(items):
    return "<ul>\n" + "\n".join("<li>%s</li>" % i for i in items) + "\n</ul>"


C = {}

# ---------------- English (root) ----------------
C["en"] = dict(
    html_lang="en",
    title="ScheduleApp Privacy Policy & Support",
    desc="ScheduleApp privacy policy and support: we collect no personal information; all data stays in your own iCloud.",
    h1="📅 ScheduleApp Privacy Policy & Support",
    meta_line=f"Effective Date: {EFFECTIVE} ｜ Developer: {DEV} ｜ Contact: {MAIL}",
    lang_label="Language:",
    in_short_label="In short:",
    summary="ScheduleApp <b>does not collect any personal information</b>. There is no account system, no developer server, and no advertising or analytics SDK. Your schedules, todos and reminders are <b>stored only in your own iCloud</b> (Apple CloudKit). Family sharing is powered by Apple's iCloud sharing; the developer cannot read or export your data.",
    nav_privacy="Privacy Policy",
    nav_faq="Support & FAQ",
    sections=(
        "<h3>1. Where is your data stored?</h3>" + ul([
            "Schedules, todos and reminder settings you create are saved <b>only in your personal iCloud database</b> (Apple CloudKit).",
            "After you create a family group, shared schedules are stored in the iCloud shared database provided by Apple and are visible only to the family members you invited.",
            "Deleting the app or signing out of iCloud does not hand your data to anyone — it remains in <b>your</b> iCloud account, managed and deletable by you through Apple.",
        ]) +
        "<h3>2. How are users identified?</h3>" + ul([
            "There is <b>no separate account system</b>. The app uses an anonymous iCloud record name provided by Apple to tell family members apart. It contains no name, email or phone number.",
            "We do <b>not</b> collect phone numbers and do <b>not</b> use SMS verification.",
        ]) +
        "<h3>3. Permissions</h3>" + ul([
            "<b>Notifications</b> — used for local due-time alerts; you can revoke at any time in Settings.",
            "<b>iCloud</b> — used for syncing and family sharing; the app also works offline without it.",
            "The app does <b>not</b> request location, contacts, camera, microphone or photo-library access.",
        ]) +
        "<h3>4. Third-party services</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — the sole provider for storage and sync, governed by Apple's privacy policy.",
            "No other third-party SDKs, no advertising, no analytics.",
        ]) +
        "<h3>5. Tracking &amp; ads</h3>" + ul([
            "We do not track users, include no tracking domains, and show no ads — as declared in the app's privacy manifest (PrivacyInfo.xcprivacy) to the App Store.",
        ]),
    ),
    faq=(
        "<h3>Will I lose my data?</h3><p>No. Data lives in your iCloud and follows your Apple account as long as iCloud is working normally.</p>" +
        "<h3>Switching to a new phone?</h3><p>Sign in with the same iCloud account on the new device and enable iCloud sync for this app — your data appears automatically.</p>" +
        "<h3>What can family members see?</h3><p>Only the schedules you publish to the family group. Your private schedules are never visible to others.</p>" +
        "<h3>Can the developer read my schedules?</h3><p>No. Data is stored in your iCloud; the developer has no access channel.</p>"
    ),
    footer=f"© {DEV} · This policy is governed by the laws applicable to the developer. For questions, email {MAIL}.",
)

# ---------------- 简体中文 ----------------
C["zh-Hans"] = dict(
    html_lang="zh-CN",
    title="日程提醒 App 隐私政策与支持",
    desc="日程提醒 App 隐私政策：我们不收集任何个人信息，全部数据仅保存在你自己的 iCloud 中。",
    h1="📅 日程提醒 隐私政策与支持",
    meta_line=f"生效日期：{EFFECTIVE} ｜ 开发者：{DEV} ｜ 联系：{MAIL}",
    lang_label="语言：",
    in_short_label="简明摘要：",
    summary="本应用<b>不收集任何个人信息</b>：无账号系统、无开发者自有服务器、无广告或统计 SDK。你的日程、待办与提醒<b>只保存在你自己的 iCloud</b>（Apple CloudKit）中；家庭共享由 Apple iCloud 共享能力提供，开发者无法读取或导出你的数据。",
    nav_privacy="隐私政策",
    nav_faq="支持与常见问题",
    sections=(
        "<h3>1. 数据存在哪里？</h3>" + ul([
            "你创建的日程、待办与提醒设置<b>只保存在你本人 iCloud 账户的私有数据库</b>（Apple CloudKit）中。",
            "创建家庭组后，共享日程保存在 Apple 提供的 iCloud 共享数据库区，仅你邀请的家庭成员可见。",
            "删除应用或退出 iCloud 登录都不会把数据交给任何人——数据始终属于<b>你的</b> iCloud 账户，由你通过 Apple 自行管理与删除。",
        ]) +
        "<h3>2. 如何区分用户？</h3>" + ul([
            "本应用<b>没有独立账号体系</b>。应用使用 Apple 提供的匿名 iCloud 记录名区分家庭成员，该标识不含姓名、邮箱或电话号码。",
            "我们<b>不</b>收集手机号，也<b>不</b>使用短信验证码。",
        ]) +
        "<h3>3. 权限说明</h3>" + ul([
            "<b>通知</b>——用于本地到点提醒，可随时在系统设置中关闭；",
            "<b>iCloud</b>——用于同步与家庭共享；不开启时应用仍可单机使用。",
            "本应用<b>不</b>申请定位、通讯录、相机、麦克风、相册权限。",
        ]) +
        "<h3>4. 第三方服务</h3>" + ul([
            "<b>Apple iCloud（CloudKit）</b>——数据存储与同步的唯一服务提供方，受 Apple 隐私政策约束。",
            "除此之外无任何第三方 SDK、无广告、无统计埋点。",
        ]) +
        "<h3>5. 追踪与广告</h3>" + ul([
            "本应用不追踪用户、不包含任何追踪域名、不投放广告（已在应用隐私清单 PrivacyInfo.xcprivacy 中向 App Store 声明）。",
        ]),
    ),
    faq=(
        "<h3>数据会丢失吗？</h3><p>不会。数据保存在你的 iCloud 中，只要 iCloud 正常，就随你的 Apple 账户保留。</p>" +
        "<h3>换新手机怎么办？</h3><p>在新设备登录同一 iCloud 账户并开启本应用的 iCloud 同步，数据会自动出现。</p>" +
        "<h3>家庭成员能看到什么？</h3><p>只有你发布到家庭组的日程；你的私有日程对其他人不可见。</p>" +
        "<h3>开发者能看到我的日程吗？</h3><p>不能。数据存在你的 iCloud 中，开发者没有访问通道。</p>"
    ),
    footer=f"© {DEV} · 如有疑问请发送邮件至 {MAIL}。",
)

# ---------------- 繁體中文（由简体转换要点手工校订） ----------------
C["zh-Hant"] = dict(
    html_lang="zh-Hant",
    title="日程提醒 App 隱私政策與支援",
    desc="日程提醒 App 隱私政策：我們不收集任何個人資訊，全部資料僅保存在你自己的 iCloud 中。",
    h1="📅 日程提醒 隱私政策與支援",
    meta_line=f"生效日期：{EFFECTIVE} ｜ 開發者：{DEV} ｜ 聯絡：{MAIL}",
    lang_label="語言：",
    in_short_label="簡明摘要：",
    summary="本應用<b>不收集任何個人資訊</b>：無帳號系統、無開發者自有伺服器、無廣告或統計 SDK。你的日程、待辦與提醒<b>只保存在你自己的 iCloud</b>（Apple CloudKit）中；家庭共享由 Apple iCloud 共享能力提供，開發者無法讀取或匯出你的資料。",
    nav_privacy="隱私政策",
    nav_faq="支援與常見問題",
    sections=(
        "<h3>1. 資料存在哪裡？</h3>" + ul([
            "你建立的日程、待辦與提醒設定<b>只保存在你本人 iCloud 帳戶的私有資料庫</b>（Apple CloudKit）中。",
            "建立家庭群組後，共享日程保存在 Apple 提供的 iCloud 共享資料庫區，僅你邀請的家庭成員可見。",
            "刪除應用程式或登出 iCloud 都不會把資料交給任何人——資料始終屬於<b>你的</b> iCloud 帳戶，由你透過 Apple 自行管理與刪除。",
        ]) +
        "<h3>2. 如何區分使用者？</h3>" + ul([
            "本應用<b>沒有獨立帳號體系</b>。應用使用 Apple 提供的匿名 iCloud 記錄名區分家庭成員，該標識不含姓名、信箱或電話號碼。",
            "我們<b>不</b>收集手機號碼，也<b>不</b>使用簡訊驗證碼。",
        ]) +
        "<h3>3. 權限說明</h3>" + ul([
            "<b>通知</b>——用於本地到點提醒，可隨時在系統設定中關閉；",
            "<b>iCloud</b>——用於同步與家庭共享；不開啟時應用仍可單機使用。",
            "本應用<b>不</b>申請定位、通訊錄、相機、麥克風、相簿權限。",
        ]) +
        "<h3>4. 第三方服務</h3>" + ul([
            "<b>Apple iCloud（CloudKit）</b>——資料儲存與同步的唯一服務提供方，受 Apple 隱私政策約束。",
            "除此之外無任何第三方 SDK、無廣告、無統計埋點。",
        ]) +
        "<h3>5. 追蹤與廣告</h3>" + ul([
            "本應用不追蹤使用者、不包含任何追蹤網域、不投放廣告（已在應用隱私清單 PrivacyInfo.xcprivacy 中向 App Store 聲明）。",
        ]),
    ),
    faq=(
        "<h3>資料會遺失嗎？</h3><p>不會。資料保存在你的 iCloud 中，只要 iCloud 正常，就隨你的 Apple 帳戶保留。</p>" +
        "<h3>換新手機怎麼辦？</h3><p>在新裝置登入同一 iCloud 帳戶並開啟本應用的 iCloud 同步，資料會自動出現。</p>" +
        "<h3>家庭成員能看到什麼？</h3><p>只有你發布到家庭群組的日程；你的私有日程對其他人不可見。</p>" +
        "<h3>開發者能看到我的日程嗎？</h3><p>不能。資料存在你的 iCloud 中，開發者沒有存取通道。</p>"
    ),
    footer=f"© {DEV} · 如有疑問請寄送郵件至 {MAIL}。",
)

# ---------------- 日本語 ----------------
C["ja"] = dict(
    html_lang="ja",
    title="ScheduleApp プライバシーポリシー＆サポート",
    desc="ScheduleApp のプライバシーポリシー：個人情報を収集せず、すべてのデータはあなた自身の iCloud に保存されます。",
    h1="📅 ScheduleApp プライバシーポリシー＆サポート",
    meta_line=f"発効日：{EFFECTIVE} ｜ 開発者：{DEV} ｜ お問い合わせ：{MAIL}",
    lang_label="言語：",
    in_short_label="要点：",
    summary="本アプリは<b>個人情報を一切収集しません</b>。アカウント登録も、開発者サーバーも、広告・解析 SDK もありません。スケジュール・ToDo・リマインダーは<b>あなた自身の iCloud</b>（Apple CloudKit）だけに保存されます。ファミリー共有は Apple の iCloud 共有機能によるもので、開発者はデータを読み書きできません。",
    nav_privacy="プライバシーポリシー",
    nav_faq="サポート・よくある質問",
    sections=(
        "<h3>1. データの保存場所</h3>" + ul([
            "作成したスケジュール・ToDo・リマインダー設定は、<b>あなたの iCloud プライベートデータベース</b>（Apple CloudKit）にのみ保存されます。",
            "ファミリーグループを作成すると、共有スケジュールは Apple 提供の iCloud 共有データベースに保存され、招待した家族だけが閲覧できます。",
            "アプリを削除したり iCloud からサインアウトしても、データは<b>あなたの</b> iCloud アカウントに属し続け、Apple 経由で管理・削除できます。",
        ]) +
        "<h3>2. ユーザーの識別方法</h3>" + ul([
            "本アプリに<b>独立したアカウント体系はありません</b>。Apple が提供する匿名の iCloud レコード名で家族を区別します。氏名・メール・電話番号は含まれません。",
            "電話番号の収集も SMS 認証も行いません。",
        ]) +
        "<h3>3. 権限について</h3>" + ul([
            "<b>通知</b> — ローカルのリマインダー用。設定でいつでもオフにできます。",
            "<b>iCloud</b> — 同期とファミリー共有用。オフでも単体で利用できます。",
            "位置情報・連絡先・カメラ・マイク・写真ライブラリの権限は<b>要求しません</b>。",
        ]) +
        "<h3>4. サードパーティサービス</h3>" + ul([
            "<b>Apple iCloud（CloudKit）</b> — 保存と同期の唯一の提供者であり、Apple のプライバシーポリシーに準拠します。",
            "その他のサードパーティ SDK・広告・解析は一切ありません。",
        ]) +
        "<h3>5. トラッキングと広告</h3>" + ul([
            "ユーザーのトラッキング、トラッキングドメイン、広告表示は一切ありません（App Store へのプライバシーマニフェスト PrivacyInfo.xcprivacy で宣言済み）。",
        ]),
    ),
    faq=(
        "<h3>データが消えることは？</h3><p>いいえ。データはあなたの iCloud にあり、iCloud が正常な限り Apple アカウントとともに保持されます。</p>" +
        "<h3>新しい iPhone に機種変更したら？</h3><p>同じ iCloud アカウントでサインインし、本アプリの iCloud 同期を有効にすると、データは自動的に表示されます。</p>" +
        "<h3>家族に見えるのは？</h3><p>ファミリーグループに公開したスケジュールだけです。非公開のスケジュールは他人に見えません。</p>" +
        "<h3>開発者はスケジュールを読めますか？</h3><p>いいえ。データはあなたの iCloud にあり、開発者にアクセス手段はありません。</p>"
    ),
    footer=f"© {DEV} · ご質問は {MAIL} まで。",
)

# ---------------- Español ----------------
C["es"] = dict(
    html_lang="es",
    title="ScheduleApp Política de privacidad y soporte",
    desc="Política de privacidad de ScheduleApp: no recogemos información personal; todos los datos permanecen en tu propio iCloud.",
    h1="📅 ScheduleApp Política de privacidad y soporte",
    meta_line=f"Fecha de vigencia: {EFFECTIVE} ｜ Desarrollador: {DEV} ｜ Contacto: {MAIL}",
    lang_label="Idioma:",
    in_short_label="En resumen:",
    summary="ScheduleApp <b>no recoge ninguna información personal</b>. No hay sistema de cuentas, ni servidores del desarrollador, ni SDK de publicidad o analíticas. Tus horarios, tareas y recordatorios se guardan <b>solo en tu propio iCloud</b> (Apple CloudKit). El uso compartido en familia se basa en el intercambio de iCloud de Apple; el desarrollador no puede leer ni exportar tus datos.",
    nav_privacy="Política de privacidad",
    nav_faq="Soporte y preguntas frecuentes",
    sections=(
        "<h3>1. ¿Dónde se guardan tus datos?</h3>" + ul([
            "Los horarios, tareas y recordatorios que creas se guardan <b>solo en tu base de datos personal de iCloud</b> (Apple CloudKit).",
            "Al crear un grupo familiar, los horarios compartidos se guardan en la base de datos compartida de iCloud proporcionada por Apple y solo los ven los miembros que invitaste.",
            "Borrar la app o cerrar sesión en iCloud no entrega tus datos a nadie: siguen siendo de <b>tu</b> cuenta de iCloud, que tú gestionas y puedes eliminar a través de Apple.",
        ]) +
        "<h3>2. ¿Cómo se identifican los usuarios?</h3>" + ul([
            "<b>No existe un sistema de cuentas propio</b>. La app distingue a los miembros de la familia mediante un nombre de registro anónimo de iCloud proporcionado por Apple, sin nombre, correo ni teléfono.",
            "<b>No</b> recogemos números de teléfono ni usamos verificación por SMS.",
        ]) +
        "<h3>3. Permisos</h3>" + ul([
            "<b>Notificaciones</b> — para alertas locales a la hora; puedes revocarlas en Ajustes en cualquier momento.",
            "<b>iCloud</b> — para sincronización y uso familiar; la app también funciona sin conexión.",
            "La app <b>no</b> solicita acceso a ubicación, contactos, cámara, micrófono ni fotos.",
        ]) +
        "<h3>4. Servicios de terceros</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — único proveedor de almacenamiento y sincronización, sujeto a la política de privacidad de Apple.",
            "Ningún otro SDK de terceros, sin publicidad ni analíticas.",
        ]) +
        "<h3>5. Rastreo y publicidad</h3>" + ul([
            "No rastreamos usuarios, sin dominios de rastreo y sin anuncios, según declaramos a App Store en la lista de privacidad (PrivacyInfo.xcprivacy).",
        ]),
    ),
    faq=(
        "<h3>¿Perderé mis datos?</h3><p>No. Los datos viven en tu iCloud y siguen a tu cuenta de Apple mientras iCloud funcione con normalidad.</p>" +
        "<h3>¿Cambio de teléfono?</h3><p>Inicia sesión con la misma cuenta de iCloud en el nuevo dispositivo y activa la sincronización iCloud de la app: tus datos aparecerán automáticamente.</p>" +
        "<h3>¿Qué pueden ver los familiares?</h3><p>Solo los horarios que publiques en el grupo familiar. Tus horarios privados nunca son visibles para otros.</p>" +
        "<h3>¿Puede el desarrollador leer mis horarios?</h3><p>No. Los datos están en tu iCloud; el desarrollador no tiene ningún canal de acceso.</p>"
    ),
    footer=f"© {DEV} · Para preguntas, escribe a {MAIL}.",
)

# ---------------- Português (BR) ----------------
C["pt-BR"] = dict(
    html_lang="pt-BR",
    title="ScheduleApp Política de Privacidade e Suporte",
    desc="Política de privacidade do ScheduleApp: não coletamos dados pessoais; todos os dados ficam no seu próprio iCloud.",
    h1="📅 ScheduleApp Política de Privacidade e Suporte",
    meta_line=f"Data de vigência: {EFFECTIVE} ｜ Desenvolvedor: {DEV} ｜ Contato: {MAIL}",
    lang_label="Idioma:",
    in_short_label="Resumo:",
    summary="O ScheduleApp <b>não coleta nenhuma informação pessoal</b>. Não há sistema de contas, servidores do desenvolvedor ou SDK de anúncios/analytics. Suas agendas, tarefas e lembretes ficam <b>somente no seu próprio iCloud</b> (Apple CloudKit). O compartilhamento familiar usa o recurso de compartilhamento do iCloud da Apple; o desenvolvedor não pode ler nem exportar seus dados.",
    nav_privacy="Política de Privacidade",
    nav_faq="Suporte e perguntas frequentes",
    sections=(
        "<h3>1. Onde seus dados ficam?</h3>" + ul([
            "Agendas, tarefas e lembretes que você cria são salvos <b>somente no seu banco de dados pessoal do iCloud</b> (Apple CloudKit).",
            "Ao criar um grupo familiar, as agendas compartilhadas ficam no banco compartilhado do iCloud fornecido pela Apple, visíveis apenas aos membros que você convidou.",
            "Apagar o app ou sair do iCloud não entrega seus dados a ninguém: eles permanecem na <b>sua</b> conta do iCloud, gerenciada e apagável por você via Apple.",
        ]) +
        "<h3>2. Como os usuários são identificados?</h3>" + ul([
            "<b>Não há sistema de contas próprio</b>. O app distingue os membros da família por um nome de registro anônimo do iCloud fornecido pela Apple, sem nome, e-mail ou telefone.",
            "<b>Não</b> coletamos números de telefone e <b>não</b> usamos verificação por SMS.",
        ]) +
        "<h3>3. Permissões</h3>" + ul([
            "<b>Notificações</b> — para alertas locais no horário; você pode revogar em Ajustes a qualquer momento.",
            "<b>iCloud</b> — para sincronização e compartilhamento familiar; o app também funciona offline.",
            "O app <b>não</b> solicita acesso a localização, contatos, câmera, microfone ou fotos.",
        ]) +
        "<h3>4. Serviços de terceiros</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — único provedor de armazenamento e sincronização, regido pela política de privacidade da Apple.",
            "Nenhum outro SDK de terceiros, sem anúncios ou analytics.",
        ]) +
        "<h3>5. Rastreamento e anúncios</h3>" + ul([
            "Não rastreamos usuários, sem domínios de rastreamento e sem anúncios — conforme declarado à App Store na lista de privacidade (PrivacyInfo.xcprivacy).",
        ]),
    ),
    faq=(
        "<h3>Vou perder meus dados?</h3><p>Não. Os dados ficam no seu iCloud e acompanham sua conta Apple enquanto o iCloud funcionar normalmente.</p>" +
        "<h3>Troquei de telefone. E agora?</h3><p>Entre com a mesma conta iCloud no novo aparelho e ative a sincronização iCloud do app: seus dados aparecem automaticamente.</p>" +
        "<h3>O que os familiares podem ver?</h3><p>Apenas as agendas que você publicar no grupo familiar. Suas agendas privadas nunca ficam visíveis para outros.</p>" +
        "<h3>O desenvolvedor pode ler minhas agendas?</h3><p>Não. Os dados estão no seu iCloud; o desenvolvedor não tem canal de acesso.</p>"
    ),
    footer=f"© {DEV} · Dúvidas: {MAIL}.",
)

# ---------------- Français ----------------
C["fr"] = dict(
    html_lang="fr",
    title="ScheduleApp Politique de confidentialité et assistance",
    desc="Politique de confidentialité de ScheduleApp : aucune donnée personnelle collectée ; tout reste dans votre propre iCloud.",
    h1="📅 ScheduleApp Politique de confidentialité et assistance",
    meta_line=f"Date d'effet : {EFFECTIVE} ｜ Développeur : {DEV} ｜ Contact : {MAIL}",
    lang_label="Langue :",
    in_short_label="En bref :",
    summary="ScheduleApp <b>ne collecte aucune donnée personnelle</b>. Pas de système de comptes, pas de serveurs du développeur, pas de SDK publicitaire ou d'analytique. Vos horaires, tâches et rappels sont stockés <b>uniquement dans votre propre iCloud</b> (Apple CloudKit). Le partage familial repose sur le partage iCloud d'Apple ; le développeur ne peut ni lire ni exporter vos données.",
    nav_privacy="Politique de confidentialité",
    nav_faq="Assistance et FAQ",
    sections=(
        "<h3>1. Où sont stockées vos données ?</h3>" + ul([
            "Les horaires, tâches et rappels que vous créez sont enregistrés <b>uniquement dans votre base de données iCloud personnelle</b> (Apple CloudKit).",
            "Après la création d'un groupe familial, les horaires partagés sont stockés dans la base partagée iCloud fournie par Apple, visibles uniquement des membres invités.",
            "Supprimer l'app ou se déconnecter d'iCloud ne remet vos données à personne : elles restent dans <b>votre</b> compte iCloud, que vous gérez et supprimez via Apple.",
        ]) +
        "<h3>2. Comment les utilisateurs sont-ils identifiés ?</h3>" + ul([
            "<b>Aucun système de comptes propre</b>. L'app distingue les membres de la famille via un nom d'enregistrement iCloud anonyme fourni par Apple, sans nom, e-mail ni téléphone.",
            "Nous ne collectons <b>aucun</b> numéro de téléphone et n'utilisons <b>aucune</b> vérification par SMS.",
        ]) +
        "<h3>3. Autorisations</h3>" + ul([
            "<b>Notifications</b> — pour les alertes locales à l'heure ; révocables à tout moment dans Réglages.",
            "<b>iCloud</b> — pour la synchronisation et le partage familial ; l'app fonctionne aussi hors ligne.",
            "L'app ne demande <b>pas</b> l'accès à la localisation, aux contacts, à la caméra, au micro ni aux photos.",
        ]) +
        "<h3>4. Services tiers</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — unique fournisseur de stockage et de synchronisation, régi par la politique de confidentialité d'Apple.",
            "Aucun autre SDK tiers, aucune publicité, aucune analytique.",
        ]) +
        "<h3>5. Suivi et publicité</h3>" + ul([
            "Aucun suivi des utilisateurs, aucun domaine de suivi, aucune publicité — déclaré à l'App Store via la liste de confidentialité (PrivacyInfo.xcprivacy).",
        ]),
    ),
    faq=(
        "<h3>Perdrai-je mes données ?</h3><p>Non. Les données vivent dans votre iCloud et suivent votre compte Apple tant qu'iCloud fonctionne normalement.</p>" +
        "<h3>Changement de téléphone ?</h3><p>Connectez-vous avec le même compte iCloud sur le nouvel appareil et activez la synchronisation iCloud de l'app : vos données apparaissent automatiquement.</p>" +
        "<h3>Que voient les membres de la famille ?</h3><p>Uniquement les horaires que vous publiez dans le groupe familial. Vos horaires privés restent invisibles pour les autres.</p>" +
        "<h3>Le développeur peut-il lire mes horaires ?</h3><p>Non. Les données sont dans votre iCloud ; le développeur n'a aucun canal d'accès.</p>"
    ),
    footer=f"© {DEV} · Questions : {MAIL}.",
)

# ---------------- Deutsch ----------------
C["de"] = dict(
    html_lang="de",
    title="ScheduleApp Datenschutzerklärung & Support",
    desc="Datenschutzerklärung von ScheduleApp: keine Erhebung personenbezogener Daten; alle Daten bleiben in deinem eigenen iCloud.",
    h1="📅 ScheduleApp Datenschutzerklärung & Support",
    meta_line=f"Gültig ab: {EFFECTIVE} ｜ Entwickler: {DEV} ｜ Kontakt: {MAIL}",
    lang_label="Sprache:",
    in_short_label="Kurz gesagt:",
    summary="ScheduleApp <b>erhebt keine personenbezogenen Daten</b>. Kein Kontosystem, keine Entwickler-Server, kein Werbe- oder Analyse-SDK. Deine Termine, Aufgaben und Erinnerungen werden <b>ausschließlich in deinem eigenen iCloud</b> (Apple CloudKit) gespeichert. Familiäres Teilen nutzt die iCloud-Freigabe von Apple; der Entwickler kann deine Daten weder lesen noch exportieren.",
    nav_privacy="Datenschutzerklärung",
    nav_faq="Support & FAQ",
    sections=(
        "<h3>1. Wo werden deine Daten gespeichert?</h3>" + ul([
            "Erstellte Termine, Aufgaben und Erinnerungen werden <b>nur in deiner persönlichen iCloud-Datenbank</b> (Apple CloudKit) gespeichert.",
            "Nach dem Anlegen einer Familiengruppe werden geteilte Termine in der von Apple bereitgestellten gemeinsamen iCloud-Datenbank gespeichert und nur von eingeladenen Mitgliedern gesehen.",
            "App löschen oder iCloud-Abmeldung übergibt deine Daten niemandem — sie bleiben in <b>deinem</b> iCloud-Konto, das du über Apple verwaltest und löschen kannst.",
        ]) +
        "<h3>2. Wie werden Nutzer unterschieden?</h3>" + ul([
            "<b>Es gibt kein eigenes Kontosystem</b>. Die App unterscheidet Familienmitglieder über einen anonymen iCloud-Datensatznamen von Apple — ohne Name, E-Mail oder Telefonnummer.",
            "Wir erheben <b>keine</b> Telefonnummern und nutzen <b>keine</b> SMS-Verifizierung.",
        ]) +
        "<h3>3. Berechtigungen</h3>" + ul([
            "<b>Mitteilungen</b> — für lokale Erinnerungen zur Terminzeit; jederzeit in den Einstellungen deaktivierbar.",
            "<b>iCloud</b> — für Sync und Familiären Freigabe; die App funktioniert auch offline.",
            "Die App fragt <b>keine</b> Berechtigung für Standort, Kontakte, Kamera, Mikrofon oder Fotos an.",
        ]) +
        "<h3>4. Dienste von Drittanbietern</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — einziger Anbieter für Speicherung und Synchronisierung, unterliegt der Datenschutzrichtlinie von Apple.",
            "Keine weiteren Drittanbieter-SDKs, keine Werbung, keine Analyse.",
        ]) +
        "<h3>5. Tracking & Werbung</h3>" + ul([
            "Kein Nutzer-Tracking, keine Tracking-Domains, keine Werbung — gegenüber dem App Store in der Datenschutzliste (PrivacyInfo.xcprivacy) erklärt.",
        ]),
    ),
    faq=(
        "<h3>Verliere ich meine Daten?</h3><p>Nein. Daten leben in deinem iCloud und folgen deinem Apple-Konto, solange iCloud normal funktioniert.</p>" +
        "<h3>Neues Telefon?</h3><p>Melde dich auf dem neuen Gerät mit demselben iCloud-Konto an und aktiviere den iCloud-Sync der App — deine Daten erscheinen automatisch.</p>" +
        "<h3>Was können Familienmitglieder sehen?</h3><p>Nur Termine, die du in der Familiengruppe veröffentlichst. Deine privaten Termine bleiben für andere unsichtbar.</p>" +
        "<h3>Kann der Entwickler meine Termine lesen?</h3><p>Nein. Daten liegen in deinem iCloud; der Entwickler hat keinen Zugriffsweg.</p>"
    ),
    footer=f"© {DEV} · Fragen an: {MAIL}.",
)

# ---------------- 한국어 ----------------
C["ko"] = dict(
    html_lang="ko",
    title="ScheduleApp 개인정보 처리방침 및 지원",
    desc="ScheduleApp 개인정보 처리방침: 개인정보를 수집하지 않으며, 모든 데이터는 사용자 자신의 iCloud에 보관됩니다.",
    h1="📅 ScheduleApp 개인정보 처리방침 및 지원",
    meta_line=f"시행일: {EFFECTIVE} ｜ 개발자: {DEV} ｜ 문의: {MAIL}",
    lang_label="언어:",
    in_short_label="요약:",
    summary="ScheduleApp은 <b>개인정보를 전혀 수집하지 않습니다</b>. 계정 체계도, 개발자 서버도, 광고·분석 SDK도 없습니다. 일정·할 일·알림은 <b>오직 사용자 자신의 iCloud</b>(Apple CloudKit)에만 저장됩니다. 가족 공유는 Apple의 iCloud 공유 기능으로 이루어지며, 개발자는 데이터를 읽거나 내보낼 수 없습니다.",
    nav_privacy="개인정보 처리방침",
    nav_faq="지원 및 자주 묻는 질문",
    sections=(
        "<h3>1. 데이터는 어디에 저장되나요?</h3>" + ul([
            "생성한 일정·할 일·알림 설정은 <b>사용자 본인의 iCloud 개인 데이터베이스</b>(Apple CloudKit)에만 저장됩니다.",
            "가족 그룹을 만들면 공유 일정은 Apple이 제공하는 iCloud 공유 데이터베이스에 저장되며, 초대한 가족만 볼 수 있습니다.",
            "앱을 삭제하거나 iCloud에서 로그아웃해도 데이터는 <b>사용자의</b> iCloud 계정에 그대로 속하며, Apple을 통해 직접 관리·삭제할 수 있습니다.",
        ]) +
        "<h3>2. 사용자를 어떻게 구분하나요?</h3>" + ul([
            "<b>별도의 계정 체계가 없습니다</b>. 앱은 Apple이 제공하는 익명 iCloud 레코드 이름으로 가족을 구분하며, 이름·이메일·전화번호를 포함하지 않습니다.",
            "전화번호를 수집하지 않고 SMS 인증도 사용하지 않습니다.",
        ]) +
        "<h3>3. 권한 안내</h3>" + ul([
            "<b>알림</b> — 로컬 정시 알림용. 시스템 설정에서 언제든 끌 수 있습니다.",
            "<b>iCloud</b> — 동기화와 가족 공유용. 꺼도 단독으로 사용할 수 있습니다.",
            "위치·연락처·카메라·마이크·사진 권한은 <b>요청하지 않습니다</b>.",
        ]) +
        "<h3>4. 서드파티 서비스</h3>" + ul([
            "<b>Apple iCloud(CloudKit)</b> — 저장과 동기화의 유일한 제공자이며 Apple 개인정보 처리방침의 적용을 받습니다.",
            "그 외 서드파티 SDK·광고·분석은 전혀 없습니다.",
        ]) +
        "<h3>5. 추적 및 광고</h3>" + ul([
            "사용자 추적 없음, 추적 도메인 없음, 광고 없음 — 앱 개인정보 명세(PrivacyInfo.xcprivacy)로 App Store에 선언되어 있습니다.",
        ]),
    ),
    faq=(
        "<h3>데이터가 사라지나요?</h3><p>아니요. 데이터는 사용자의 iCloud에 있으며 iCloud가 정상인 한 Apple 계정과 함께 유지됩니다.</p>" +
        "<h3>새 폰으로 바꾸면?</h3><p>새 기기에서 같은 iCloud 계정으로 로그인하고 앱의 iCloud 동기화를 켜면 데이터가 자동으로 나타납니다.</p>" +
        "<h3>가족은 무엇을 볼 수 있나요?</h3><p>가족 그룹에 발행한 일정만 볼 수 있습니다. 개인 일정은 다른 사람에게 보이지 않습니다.</p>" +
        "<h3>개발자가 내 일정을 볼 수 있나요?</h3><p>볼 수 없습니다. 데이터는 사용자의 iCloud에 있으며 개발자에게는 접근 경로가 없습니다.</p>"
    ),
    footer=f"© {DEV} · 문의: {MAIL}.",
)

# ---------------- Русский ----------------
C["ru"] = dict(
    html_lang="ru",
    title="ScheduleApp Политика конфиденциальности и поддержка",
    desc="Политика конфиденциальности ScheduleApp: мы не собираем персональные данные; все данные хранятся только в вашем iCloud.",
    h1="📅 ScheduleApp Политика конфиденциальности и поддержка",
    meta_line=f"Дата вступления в силу: {EFFECTIVE} ｜ Разработчик: {DEV} ｜ Контакты: {MAIL}",
    lang_label="Язык:",
    in_short_label="Кратко:",
    summary="ScheduleApp <b>не собирает персональные данные</b>: нет системы аккаунтов, нет серверов разработчика, нет рекламных или аналитических SDK. Ваши расписания, задачи и напоминания хранятся <b>только в вашем собственном iCloud</b> (Apple CloudKit). Семейный доступ работает через механизм обмена iCloud от Apple; разработчик не может читать или экспортировать ваши данные.",
    nav_privacy="Политика конфиденциальности",
    nav_faq="Поддержка и частые вопросы",
    sections=(
        "<h3>1. Где хранятся ваши данные?</h3>" + ul([
            "Созданные расписания, задачи и настройки напоминаний сохраняются <b>только в вашей личной базе данных iCloud</b> (Apple CloudKit).",
            "После создания семейной группы общие расписания хранятся в общей базе iCloud, предоставляемой Apple, и видны только приглашённым участникам.",
            "Удаление приложения или выход из iCloud не передаёт данные никому — они остаются в <b>вашем</b> аккаунте iCloud, управление и удаление — через Apple.",
        ]) +
        "<h3>2. Как различаются пользователи?</h3>" + ul([
            "<b>Отдельной системы аккаунтов нет</b>. Приложение различает членов семьи по анонимному имени записи iCloud, предоставляемому Apple, — без имени, e-mail или телефона.",
            "Мы <b>не</b> собираем номера телефонов и <b>не</b> используем SMS-код подтверждения.",
        ]) +
        "<h3>3. Разрешения</h3>" + ul([
            "<b>Уведомления</b> — для локальных напоминаний по времени; можно отключить в Настройках в любой момент.",
            "<b>iCloud</b> — для синхронизации и семейного доступа; без него приложение работает автономно.",
            "Приложение <b>не</b> запрашивает доступ к геолокации, контактам, камере, микрофону и фото.",
        ]) +
        "<h3>4. Сторонние сервисы</h3>" + ul([
            "<b>Apple iCloud (CloudKit)</b> — единственный поставщик хранения и синхронизации, подчиняется политике конфиденциальности Apple.",
            "Никаких других сторонних SDK, рекламы или аналитики.",
        ]) +
        "<h3>5. Отслеживание и реклама</h3>" + ul([
            "Мы не отслеживаем пользователей, не используем домены отслеживания и не показываем рекламу — что заявлено App Store в манифесте конфиденциальности (PrivacyInfo.xcprivacy).",
        ]),
    ),
    faq=(
        "<h3>Потеряю ли я данные?</h3><p>Нет. Данные живут в вашем iCloud и следуют за вашим Apple-аккаунтом, пока iCloud работает нормально.</p>" +
        "<h3>Смена телефона?</h3><p>Войдите на новом устройстве в тот же аккаунт iCloud и включите синхронизацию iCloud в приложении — данные появятся автоматически.</p>" +
        "<h3>Что видят члены семьи?</h3><p>Только расписания, опубликованные в семейную группу. Личные расписания никто другой не видит.</p>" +
        "<h3>Может ли разработчик читать мои расписания?</h3><p>Нет. Данные хранятся в вашем iCloud; у разработчика нет канала доступа.</p>"
    ),
    footer=f"© {DEV} · Вопросы: {MAIL}.",
)


def main():
    # 根目录 = 英文（ASC「隐私政策网址」直接填站点根）
    open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(page(C["en"]))
    for lang in LANGS:
        d = os.path.join(BASE, lang)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(C[lang]))
    print("generated:", ", ".join(LANGS), "+ root(en) ->", BASE)


if __name__ == "__main__":
    main()
