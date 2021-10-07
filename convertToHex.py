  def toHex(self, num: int) -> str:
      dec_to_hex = {'10':'a', '11':'b', '12':'c',
                    '13':'d', '14':'e', '15':'f'}
      res = deque()

      if not num:
          return "0"

      if num < 0:
          num += 2**32

      while num:
          num, rem = divmod(num, 16)
          rem = str(rem)
          if rem in dec_to_hex:
              rem = dec_to_hex[rem]
          res.appendleft(rem)

      return ''.join(res)
