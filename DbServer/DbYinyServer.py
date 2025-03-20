import DbServer.DbDomServer as Dds
import Config.ConfigServer as Cs
from OutPut.outPut import op


class DbYinyServer:
    def __init__(self):
        pass

    def addPushYiny(self, yinyId, yinyName):
        """
        新增推送群聊
        :param yinyName:
        :param yinyId:
        :return:
        """
        conn, cursor = Dds.openDb(Cs.returnYinyDbPath())
        try:
            if not self.searchPushYiny(yinyId):
                cursor.execute('INSERT INTO pushYiny VALUES (?, ?)', (yinyId, yinyName))
                conn.commit()
                Dds.closeDb(conn, cursor)
                return True
            return False
        except Exception as e:
            op(f'[-]: 新增推送群聊出现错误, 错误信息: {e}')
            Dds.closeDb(conn, cursor)
            return False

    def searchPushYiny(self, yinyId):
        """
        查询推送群聊
        :param yinyId:
        :return:
        """
        conn, cursor = Dds.openDb(Cs.returnYinyDbPath())
        try:
            cursor.execute('SELECT yinyName FROM pushYiny WHERE yinyId=?', (yinyId,))
            result = cursor.fetchone()
            Dds.closeDb(conn, cursor)
            if result:
                return result
            else:
                return False
        except Exception as e:
            op(f'[-]: 查询推送群聊出现错误, 错误信息: {e}')
            Dds.closeDb(conn, cursor)
            return False
    def showPushYiny(self, ):
        """
        查看所有推送群聊
        :return:
        """
        conn, cursor = Dds.openDb(Cs.returnYinyDbPath())
        dataDict = dict()
        try:
            cursor.execute('SELECT yinyId, yinyName FROM pushYiny')
            result = cursor.fetchall()
            Dds.closeDb(conn, cursor)
            if result:
                for res in result:
                    dataDict[res[0]] = res[1]
            return dataDict
        except Exception as e:
            op(f'[-]: 查看所有黑名单群聊出现错误, 错误信息: {e}')
            Dds.closeDb(conn, cursor)
            return dataDict