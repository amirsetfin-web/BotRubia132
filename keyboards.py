# -*- coding: utf-8 -*-
from rubka.keypad import ChatKeypadBuilder
from rubka.button import InlineBuilder
import config

BTN_TICKET = "🎫 تیکت"
BTN_FAQ = "❓ سوالات متداول شما"
BTN_NEW_TICKET = "➕ ساخت تیکت"
BTN_MY_TICKETS = "📂 تیکت‌های من"
BTN_BACK_MAIN = "⬅️ بازگشت به منو"
BTN_BACK = "⬅️ بازگشت"
BTN_CLOSE_TICKET = "🔒 بستن تیکت"

BTN_FAQ_NEW = "➕ ساخت سوال"
BTN_FAQ_LIST = "📚 دیدن تمامی سوال‌ها"

BTN_PANEL = "🛠 پنل Staff"
BTN_MANAGE = "🎫 مدیریت تیکت‌ها"
BTN_MINE = "👤 تیکت‌های من"
BTN_STATS_ME = "📊 آمار من"
BTN_STATS_SYS = "📈 آمار سیستم"
BTN_STAFF_MGMT = "👨‍💼 مدیریت Staff"
BTN_ALERT = "🚨 ارسال اعلان"
BTN_UNANSWERED = "❗ بدون پاسخ"
BTN_STALE = "⏰ تیکت‌های معطل"
BTN_SEARCH = "🔍 جستجوی تیکت"

BTN_ADD_STAFF = "➕ افزودن Staff جدید"
BTN_CHANGE_RANK = "🔄 تغییر رنک Staff"
BTN_REMOVE_STAFF = "➖ حذف Staff"
BTN_LIST_STAFF = "📋 لیست Staffها"

BTN_ALERT_STAFF = "📢 به همه Staffها"
BTN_ALERT_USERS = "📢 به همه کاربران"

RATING_LABELS = ["⭐ 1", "⭐ 2", "⭐ 3", "⭐ 4", "⭐ 5"]


def _chat_kb(*rows_of_labels):
    """هر عنصر rows_of_labels یک لیست از برچسب‌های دکمه برای یک ردیفه."""
    b = ChatKeypadBuilder()
    rows = []
    for labels in rows_of_labels:
        rows.append(b.row(*[b.button(id=label, text=label) for label in labels]))
    # ساخت نهایی: هر row() قبلاً به builder اضافه شده، پس فقط build می‌کنیم
    return b.build()


def main_menu_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_TICKET, text=BTN_TICKET))
    b.row(b.button(id=BTN_FAQ, text=BTN_FAQ))
    return b.build()


def staff_home_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_PANEL, text=BTN_PANEL))
    return b.build()


def ticket_menu_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_NEW_TICKET, text=BTN_NEW_TICKET))
    b.row(b.button(id=BTN_MY_TICKETS, text=BTN_MY_TICKETS))
    b.row(b.button(id=BTN_BACK_MAIN, text=BTN_BACK_MAIN))
    return b.build()


def in_ticket_chat_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_BACK_MAIN, text=BTN_BACK_MAIN), b.button(id=BTN_CLOSE_TICKET, text=BTN_CLOSE_TICKET))
    return b.build()


def staff_in_ticket_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_CLOSE_TICKET, text=BTN_CLOSE_TICKET), b.button(id=BTN_BACK, text=BTN_BACK))
    return b.build()


def faq_menu_keypad(can_create=False):
    b = ChatKeypadBuilder()
    if can_create:
        b.row(b.button(id=BTN_FAQ_NEW, text=BTN_FAQ_NEW))
    b.row(b.button(id=BTN_FAQ_LIST, text=BTN_FAQ_LIST))
    b.row(b.button(id=BTN_BACK_MAIN, text=BTN_BACK_MAIN))
    return b.build()


def rating_inline_keypad(ticket_id):
    ib = InlineBuilder()
    ib.row(*[ib.button_simple(f"rate_{ticket_id}_{i}", t) for i, t in enumerate(RATING_LABELS, start=1)])
    return ib.build()


def review_choice_inline_keypad(ticket_id):
    ib = InlineBuilder()
    ib.row(ib.button_simple(f"revw_{ticket_id}", "📝 ثبت نظر"), ib.button_simple(f"revs_{ticket_id}", "⏭ بدون نظر"))
    return ib.build()


def confirm_close_inline_keypad(ticket_id):
    ib = InlineBuilder()
    ib.row(ib.button_simple(f"userclose_yes_{ticket_id}", "✅ بله، مطمئنم"),
           ib.button_simple(f"userclose_no_{ticket_id}", "❌ نه، منصرف شدم"))
    return ib.build()


def faq_preview_inline_keypad():
    ib = InlineBuilder()
    ib.row(ib.button_simple("faq_edit_q", "✏️ ویرایش سوال"))
    ib.row(ib.button_simple("faq_edit_a", "✏️ ویرایش جواب"))
    ib.row(ib.button_simple("faq_submit", "✅ ثبت"))
    return ib.build()


def faq_list_inline_keypad(items):
    ib = InlineBuilder()
    for it in items:
        short = it["question"] if len(it["question"]) <= 40 else it["question"][:37] + "..."
        ib.row(ib.button_simple(f"faqv_{it['id']}", f"❓ {short}"))
    return ib.build()


def user_tickets_list_inline_keypad(tickets):
    ib = InlineBuilder()
    for t in tickets:
        label = "🔴 باز" if t["status"] != "CLOSED" else "✅ بسته"
        ib.row(ib.button_simple(f"myticket_{t['id']}", f"🎫 #{t['id']} — {label}"))
    return ib.build()


def all_my_tickets_inline_keypad():
    ib = InlineBuilder()
    ib.row(ib.button_simple("all_my_tickets", "📂 دیدن تمامی تیکت‌ها"))
    return ib.build()


# ---------------- پنل Staff ----------------
def staff_panel_keypad(rank):
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_MANAGE, text=BTN_MANAGE))
    b.row(b.button(id=BTN_MINE, text=BTN_MINE))
    b.row(b.button(id=BTN_FAQ, text=BTN_FAQ))
    b.row(b.button(id=BTN_STATS_ME, text=BTN_STATS_ME))
    b.row(b.button(id=BTN_UNANSWERED, text=BTN_UNANSWERED), b.button(id=BTN_STALE, text=BTN_STALE))
    b.row(b.button(id=BTN_SEARCH, text=BTN_SEARCH))
    if config.RANK_LEVEL.get(rank, 0) >= config.RANK_LEVEL[config.RANK_ADMIN]:
        b.row(b.button(id=BTN_STATS_SYS, text=BTN_STATS_SYS), b.button(id=BTN_ALERT, text=BTN_ALERT))
    if config.RANK_LEVEL.get(rank, 0) >= config.RANK_LEVEL[config.RANK_MANAGER]:
        b.row(b.button(id=BTN_STAFF_MGMT, text=BTN_STAFF_MGMT))
    b.row(b.button(id=BTN_BACK_MAIN, text=BTN_BACK_MAIN))
    return b.build()


TICKET_FILTER_BUTTONS = [
    ("🆕 جدید", "new"),
    ("⏳ منتظر پاسخ Staff", "waiting_staff"),
    ("💬 در حال پاسخ‌گویی", "in_progress"),
    ("📨 منتظر پاسخ کاربر", "waiting_user"),
    ("🔴 باز", "open"),
    ("🔒 بسته‌شده", "closed"),
    ("📂 همه", "all"),
]


def ticket_management_keypad(counts):
    b = ChatKeypadBuilder()
    for label, key in TICKET_FILTER_BUTTONS:
        full = f"{label} ({counts.get(key, 0)})"
        b.row(b.button(id=full, text=full))
    b.row(b.button(id=BTN_BACK, text=BTN_BACK))
    return b.build()


def tickets_list_inline_keypad(tickets):
    ib = InlineBuilder()
    for t in tickets:
        label = config.STATUS_LABELS_FA.get(t["status"], t["status"])
        ib.row(ib.button_simple(f"view_{t['id']}", f"🎫 #{t['id']} — {label}"))
    return ib.build()


def ticket_action_inline_keypad(ticket_id, is_owner):
    ib = InlineBuilder()
    if is_owner:
        ib.row(ib.button_simple(f"transfer_{ticket_id}", "🔄 انتقال"))
        ib.row(ib.button_simple(f"note_{ticket_id}", "📝 یادداشت داخلی"))
    else:
        ib.row(ib.button_simple(f"claim_{ticket_id}", "👤 دریافت تیکت"))
    ib.row(ib.button_simple(f"uinfo_{ticket_id}", "👤 اطلاعات کاربر"), ib.button_simple(f"hist_{ticket_id}", "📜 تاریخچه"))
    return ib.build()


def busy_staff_inline_keypad(active_ticket_id):
    ib = InlineBuilder()
    ib.row(ib.button_simple(f"view_{active_ticket_id}", "🎫 ورود به تیکت فعلی"))
    ib.row(ib.button_simple(f"close_{active_ticket_id}", "🔒 بستن تیکت"))
    ib.row(ib.button_simple(f"transfer_{active_ticket_id}", "🔄 انتقال تیکت"))
    return ib.build()


def new_ticket_notification_inline_keypad(ticket_id):
    ib = InlineBuilder()
    ib.row(ib.button_simple(f"claim_{ticket_id}", "👀 مشاهده تیکت"))
    return ib.build()


def staff_mgmt_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_ADD_STAFF, text=BTN_ADD_STAFF))
    b.row(b.button(id=BTN_CHANGE_RANK, text=BTN_CHANGE_RANK))
    b.row(b.button(id=BTN_REMOVE_STAFF, text=BTN_REMOVE_STAFF))
    b.row(b.button(id=BTN_LIST_STAFF, text=BTN_LIST_STAFF))
    b.row(b.button(id=BTN_BACK, text=BTN_BACK))
    return b.build()


def alert_menu_keypad():
    b = ChatKeypadBuilder()
    b.row(b.button(id=BTN_ALERT_STAFF, text=BTN_ALERT_STAFF))
    b.row(b.button(id=BTN_ALERT_USERS, text=BTN_ALERT_USERS))
    b.row(b.button(id=BTN_BACK, text=BTN_BACK))
    return b.build()


def rank_pick_inline_keypad(target_id):
    ib = InlineBuilder()
    for r in config.RANK_LEVEL.keys():
        ib.row(ib.button_simple(f"setrank_{target_id}_{r}", config.RANK_LABELS_FA[r]))
    return ib.build()


def staff_pick_inline_keypad(staff_ids, display_name_fn):
    ib = InlineBuilder()
    for sid in staff_ids:
        ib.row(ib.button_simple(f"pickrank_{sid}", display_name_fn(sid)))
    return ib.build()


def transfer_pick_inline_keypad(ticket_id, staff_ids, display_name_fn):
    ib = InlineBuilder()
    for sid in staff_ids:
        ib.row(ib.button_simple(f"doT_{ticket_id}_{sid}", f"➡️ {display_name_fn(sid)}"))
    return ib.build()
