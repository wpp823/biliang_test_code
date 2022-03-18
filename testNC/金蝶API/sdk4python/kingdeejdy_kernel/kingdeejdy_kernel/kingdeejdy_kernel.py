# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time

from Tea.core import TeaCore
from Tea.exceptions import TeaException, UnretryableException
from Tea.model import TeaModel
from Tea.request import TeaRequest
from Tea.response import TeaResponse
from alibabacloud_tea_util.client import Client as UtilClient


class KingdeejdyKernel:
    _server_host: str = None
    _account_id: str = None
    _group_name: str = None
    _protocol: str = None
    _headers: dict = None
    _query: dict = None

    def __init__(self, access_token: str, account_id: str, group_name: str, ):
        """
        init the client
        @param config: Config of the config
        """
        self._server_host = 'api.kingdee.com'
        self._protocol = 'https'
        self._headers = {
            'accountId': access_token,
            'groupName': group_name
        }
        self._account_id = account_id
        self._group_name = group_name
        self._query = {
            'access_token': access_token
        }

    def _get(self, pathname: str, headers: TeaModel, query: TeaModel, ) -> dict:
        """
        the api use to deal with get request
        @param pathname: pathname of the get api
        @param query: the model of query params
        @return: result result of the server
        """
        headers.validate()
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'GET'
                _request.protocol = self._protocol
                _request.pathname = pathname
                _request.headers = {
                    'host': self._server_host
                }
                headers_map = UtilClient.stringify_map_value(TeaCore.to_map(query))
                if not UtilClient.empty(headers_map.get('accountId')):
                    _request.headers['accountId'] = headers_map.get('accountId')
                if not UtilClient.empty(headers_map.get('groupName')):
                    _request.headers['groupName'] = headers_map.get('groupName')
                _request.query = UtilClient.stringify_map_value(TeaCore.to_map(query))
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                return self._handle(_response)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def _get_async(self, pathname: str, headers: TeaModel, query: TeaModel, ) -> dict:
        """
        the api use to deal with get request
        @param pathname: pathname of the get api
        @param query: the model of query params
        @return: result result of the server
        """
        headers.validate()
        query.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'GET'
                _request.protocol = self._protocol
                _request.pathname = pathname
                _request.headers = {
                    'host': self._server_host
                }
                headers_map = UtilClient.stringify_map_value(TeaCore.to_map(query))
                if not UtilClient.empty(headers_map.get('accountId')):
                    _request.headers['accountId'] = headers_map.get('accountId')
                if not UtilClient.empty(headers_map.get('groupName')):
                    _request.headers['groupName'] = headers_map.get('groupName')
                _request.query = UtilClient.stringify_map_value(TeaCore.to_map(query))
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                return await self._handle_async(_response)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def _post(self, pathname: str, body: TeaModel, ) -> dict:
        """
        the api use to deal with post request
        @param pathname: pathname of the post api
        @param query: the model of body params
        @param body: the model of body body
        @return: result result of the server
        """
        body.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'POST'
                _request.protocol = self._protocol
                _request.pathname = pathname
                _request.headers = {
                    'host': self._server_host,
                    'content-type': 'application/json; charset=utf-8',
                    'accountId': self._account_id,
                    'groupName': self._group_name
                }
                _request.body = UtilClient.to_jsonstring(TeaCore.to_map(body))
                _request.query = UtilClient.stringify_map_value(self._query)
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                return self._handle(_response)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    async def _post_async(self, pathname: str, body: TeaModel, ) -> dict:
        """
        the api use to deal with post request
        @param pathname: pathname of the post api
        @param query: the model of body params
        @param body: the model of body body
        @return: result result of the server
        """
        body.validate()
        _runtime = {
            'connectTimeout': 15000,
            'readTimeout': 15000,
            'retry': {
                'maxAttempts': 0
            }
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get('retry'), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(_runtime.get('backoff'), _retry_times)
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.method = 'POST'
                _request.protocol = self._protocol
                _request.pathname = pathname
                _request.headers = {
                    'host': self._server_host,
                    'content-type': 'application/json; charset=utf-8',
                    'accountId': self._account_id,
                    'groupName': self._group_name
                }
                _request.body = UtilClient.to_jsonstring(TeaCore.to_map(body))
                _request.query = UtilClient.stringify_map_value(self._query)
                _last_request = _request
                _response = await TeaCore.async_do_action(_request, _runtime)
                return await self._handle_async(_response)
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)

    def get(self, api: str, query: TeaModel, ) -> dict:
        return self._get(api, None, query)

    async def get_async(self, api: str, query: TeaModel, ) -> dict:
        return await self._get_async(api, None, query)

    def post(self, api: str, body: TeaModel, ) -> dict:
        return self._post(api, body)

    async def post_async(self, api: str, body: TeaModel, ) -> dict:
        return await self._post_async(api, body)

    def _handle(self, response: TeaResponse, ) -> dict:
        """
        the handler use to deal with the response
        @param response: from tea repository server
        @return: result result of the server
        """
        result = UtilClient.assert_as_map(UtilClient.read_as_json(response.body))
        if not UtilClient.equal_number(response.status_code, 200):
            if UtilClient.equal_number(response.status_code, 519):
                raise TeaException({
                    'message': f"code: {response.status_code}, {result.get('code')} reason: {result.get('description_cn')}",
                    'code': f"{result.get('code')}"
                })
            raise TeaException({
                'message': f"code: {response.status_code}, {result.get('code')} reason: {result.get('message')}",
                'code': f"{result.get('code')}"
            })
        return result

    async def _handle_async(self, response: TeaResponse, ) -> dict:
        """
        the handler use to deal with the response
        @param response: from tea repository server
        @return: result result of the server
        """
        result = UtilClient.assert_as_map(await UtilClient.read_as_json_async(response.body))
        if not UtilClient.equal_number(response.status_code, 200):
            if UtilClient.equal_number(response.status_code, 519):
                raise TeaException({
                    'message': f"code: {response.status_code}, {result.get('code')} reason: {result.get('description_cn')}",
                    'code': f"{result.get('code')}"
                })
            raise TeaException({
                'message': f"code: {response.status_code}, {result.get('code')} reason: {result.get('message')}",
                'code': f"{result.get('code')}"
            })
        return result
