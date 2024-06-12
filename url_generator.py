def get_video_id_from_file(content):
    reference = content.find("forFriend")
    start = content.find("'id':", reference) + 7
    end = start + 19
    video_id = content[start:end]
    return video_id

def get_unique_id_from_file(content):
    start = content.find("uniqueId") + 12
    end = content.find("verified", start) - 4
    unique_id = content[start: end]
    return unique_id

def generate_url(content):
    unique_id = get_unique_id_from_file(content)
    video_id = get_video_id_from_file(content)
    url = f"https://www.tiktok.com/@{unique_id}/video/{video_id}"
    return url   