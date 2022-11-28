from __future__ import annotations

import json
from config import CANDIDATES


def load_candidates() -> list[dict] | None:
    """
    Load candidates data from json-file

    Returns:
        data: list of dicts with data if successful
        None: if raises FileNotFoundError
    Raises:
        FileNotFoundError: if the file is not found
    """
    try:
        with open(CANDIDATES, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None


def get_candidate(candidate_id: int) -> dict | None:
    """
    Get candidate data by primary key

    Args:
        candidate_id: candidat primary key
    Returns:
        dict with candidate's data or None
    """
    all_candidates = load_candidates()
    if all_candidates:
        for candidate in all_candidates:
            if candidate['id'] == candidate_id:
                return candidate
    return None


def get_candidates_by_name(candidate_name: str) -> list[dict] | []:
    """
    Search candidates by name

    Args:
        candidate_name: name to search
    Returns:
        list of dicts with candidates or empty list
    """
    all_candidates = load_candidates()
    found_by_name = []
    for candidate in all_candidates:
        if candidate_name.lower() in candidate['name'].lower():
            found_by_name.append(candidate)
    return found_by_name


def get_candidates_by_skill(skill_name: str) -> list[dict] | []:
    """
    Search candidates by skill

    Args:
        skill_name: skill to search
    Returns:
        list of dicts with candidates or empty list
    """
    all_candidates = load_candidates()
    found_by_skill = []
    for candidate in all_candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            found_by_skill.append(candidate)
    return found_by_skill
