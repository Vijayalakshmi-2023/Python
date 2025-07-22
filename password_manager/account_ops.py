# account_ops.py

def add_account(accounts, site, username, password, tags):
    if site in accounts:
        return f"⚠️ Site '{site}' already exists."
    accounts[site] = {
        "credentials": (username, password),
        "tags": set(tags)
    }
    return f"✅ Added account for '{site}'"

def update_account(accounts, site, username=None, password=None, tags=None):
    if site not in accounts:
        return f"❌ No such site: '{site}'"
    
    user, pwd = accounts[site]["credentials"]
    accounts[site]["credentials"] = (
        username if username else user,
        password if password else pwd
    )
    if tags:
        accounts[site]["tags"].update(tags)
    return f"🔄 Updated account for '{site}'"

def delete_account(accounts, site):
    if site in accounts:
        del accounts[site]
        return f"🗑️ Deleted account for '{site}'"
    return f"❌ Site '{site}' not found."

def search_by_tag(accounts, tag):
    results = {
        site: info for site, info in accounts.items()
        if tag in info["tags"]
    }
    return results

def search_by_site(accounts, site):
    return accounts.get(site, None)

def format_account(site, info):
    user, pwd = info["credentials"]
    tags = ", ".join(info["tags"])
    return f"{site} → User: {user}, Pass: {pwd}, Tags: [{tags}]"
