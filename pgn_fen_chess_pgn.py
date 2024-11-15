
import chess
import chess.pgn

def tabla_de_tableros(posicion):

    # un movimiento
    fotograma = []

    # ['rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1']
    FEN = posicion.split(' ')

    # ['r1b1kbnr', 'ppppqppp', '2n5', '4P3', '8', '5N2', 'PPP1PPPP', 'RNBQKB1R']
    FEN = FEN[0].split('/')  # una lista de filas

    for fila_fen in FEN:

        fila_tablero = []
        for casilla in fila_fen:

            if casilla.isnumeric():
                con = int(casilla)
                while con > 0:
                    fila_tablero.append(' ')
                    con -= 1
            elif casilla.isalpha():
                fila_tablero.append(casilla)

            # [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            #  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            #  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            #  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        fotograma.append(fila_tablero)        
    return fotograma


def descarga_partida(archivo):
    '''Lee el archivo y crea las posiciones''' 
    with open(archivo,'r',encoding="utf-8") as pgn:
        primer_juego = chess.pgn.read_game(pgn)
        _ = chess.Board()
        # Iterate through all moves and play them on a board.
        # Repita todos los movimientos y reprodúzcalos en un tablero.
        board = primer_juego.board()
        list_movi=['inicio']
        list_fen = [board.fen()]
        for move in primer_juego.mainline_moves():
            mobo=board.san(move)
            board.push(move)
            posicion=board.fen()
            list_movi.append(mobo)
            list_fen.append(posicion)

        return list_movi, list_fen

if __name__ == '__main__':
    notaciones_algebraicas, posiciones_fen= descarga_partida(
        'lichess_pgn_2024.10.30_LIFTISTO_vs_israel_ima.6sfvWFd7.pgn')   
    partida = zip(notaciones_algebraicas, posiciones_fen)
    for jugada, posicion_fen in partida:
        tablero= tabla_de_tableros(posicion_fen)
        print(jugada)
        print(posicion_fen)
        for fila in tablero:
            print(fila)
        input()
