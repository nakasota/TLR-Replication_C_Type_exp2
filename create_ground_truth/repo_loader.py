#!/usr/bin/env python3
"""
Goリポジトリローダー
現在のGoリポジトリからファイル内容を取得する
"""

import json
import requests
import os
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class GoRepoLoader:
    """
    Goリポジトリからファイル内容を取得するローダー
    """
    
    def __init__(self, repo_structure_path: str = None):
        """
        Args:
            repo_structure_path: リポジトリ構造JSONファイルのパス
        """
        self.repo_structure_path = repo_structure_path or "../data/ground_truth/go_repo_structure.json"
        self.repo_structure = None
        self.github_api_base = "https://api.github.com/repos/golang/go/contents"
        self.raw_github_base = "https://raw.githubusercontent.com/golang/go/master"
        self._load_repo_structure()
    
    def _load_repo_structure(self):
        """リポジトリ構造を読み込み"""
        try:
            if os.path.exists(self.repo_structure_path):
                with open(self.repo_structure_path, 'r', encoding='utf-8') as f:
                    self.repo_structure = json.load(f)
                logger.info(f"Repository structure loaded: {len(self.repo_structure)} files")
            else:
                logger.warning(f"Repository structure file not found: {self.repo_structure_path}")
                self.repo_structure = {}
        except Exception as e:
            logger.error(f"Error loading repository structure: {str(e)}")
            self.repo_structure = {}
    
    def get_file_content(self, file_path: str) -> Optional[str]:
        """
        指定されたファイルパスの内容を取得
        
        Args:
            file_path: ファイルパス（例: "src/cmd/go/internal/test/test.go"）
            
        Returns:
            ファイル内容（文字列）、取得できない場合はNone
        """
        try:
            # ファイルパスを正規化
            normalized_path = self._normalize_file_path(file_path)
            
            # リポジトリ構造に存在するかチェック
            if self.repo_structure and normalized_path not in self.repo_structure:
                logger.debug(f"File not found in repository structure: {normalized_path}")
                return None
            
            # GitHub APIを使用してファイル内容を取得
            content = self._fetch_from_github(normalized_path)
            if content:
                return content
            
            # フォールバック: raw.githubusercontent.comから取得
            content = self._fetch_from_raw_github(normalized_path)
            if content:
                return content
            
            logger.debug(f"Failed to fetch file content: {normalized_path}")
            return None
            
        except Exception as e:
            logger.debug(f"Error getting file content for {file_path}: {str(e)}")
            return None
    
    def _normalize_file_path(self, file_path: str) -> str:
        """
        ファイルパスを正規化
        """
        # 先頭のスラッシュを除去
        normalized = file_path.lstrip('/')
        
        # src/プレフィックスを追加（必要に応じて）
        if not normalized.startswith('src/') and not normalized.startswith('test/'):
            # パスによって適切なプレフィックスを判定
            if 'cmd/' in normalized or 'internal/' in normalized:
                normalized = f"src/{normalized}"
        
        return normalized
    
    def _fetch_from_github(self, file_path: str) -> Optional[str]:
        """
        GitHub APIからファイル内容を取得
        """
        try:
            url = f"{self.github_api_base}/{file_path}"
            
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                data = response.json()
                if data.get('type') == 'file' and 'content' in data:
                    import base64
                    content = base64.b64decode(data['content']).decode('utf-8')
                    logger.debug(f"Successfully fetched from GitHub API: {file_path}")
                    return content
            
            logger.debug(f"GitHub API request failed: {response.status_code} for {file_path}")
            return None
            
        except Exception as e:
            logger.debug(f"Error fetching from GitHub API: {str(e)}")
            return None
    
    def _fetch_from_raw_github(self, file_path: str) -> Optional[str]:
        """
        raw.githubusercontent.comからファイル内容を取得
        """
        try:
            url = f"{self.raw_github_base}/{file_path}"
            
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                logger.debug(f"Successfully fetched from raw GitHub: {file_path}")
                return response.text
            
            logger.debug(f"Raw GitHub request failed: {response.status_code} for {file_path}")
            return None
            
        except Exception as e:
            logger.debug(f"Error fetching from raw GitHub: {str(e)}")
            return None
    
    def file_exists(self, file_path: str) -> bool:
        """
        ファイルが存在するかチェック
        """
        normalized_path = self._normalize_file_path(file_path)
        return normalized_path in (self.repo_structure or {})
    
    def get_file_info(self, file_path: str) -> Optional[Dict[str, Any]]:
        """
        ファイル情報を取得
        """
        normalized_path = self._normalize_file_path(file_path)
        return (self.repo_structure or {}).get(normalized_path)
