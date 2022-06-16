import arrow

# end_at = arrow.now()
begin_at = arrow.get('2022-05-11 16:37:27')
end_at = arrow.get('2022-05-11 16:50:27')

diff_time = end_at - begin_at
print(diff_time.seconds)
