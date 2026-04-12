export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-900 text-slate-50">
      <main className="w-full max-w-3xl rounded-2xl border border-slate-700 bg-slate-950/80 p-8 shadow-xl">
        <h1 className="text-2xl font-semibold tracking-wide">
          2025年3月 カレンダー（ダミー）
        </h1>
        <p className="mt-2 text-sm text-slate-300">
          これは OpenCal 用の、シンプルな 3 月カレンダーのフロント実装サンプルです。
        </p>

        <section className="mt-6">
          <div className="grid grid-cols-7 text-center text-xs font-semibold uppercase tracking-[0.2em] text-slate-400">
            <div>日</div>
            <div>月</div>
            <div>火</div>
            <div>水</div>
            <div>木</div>
            <div>金</div>
            <div>土</div>
          </div>

          <div className="mt-2 grid grid-cols-7 gap-1 text-sm">
            {/* 1週目（3月1日が土曜想定） */}
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40" />
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40" />
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40" />
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40" />
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40" />
            <div className="h-20 rounded-lg border border-slate-800/60 bg-slate-900/40 flex flex-col items-end p-1">
              <span className="text-xs text-slate-300">1</span>
            </div>
            <div className="h-20 rounded-lg border border-slate-800/60 bg-emerald-900/50 flex flex-col items-end p-1">
              <span className="text-xs text-slate-50">2</span>
              <span className="mt-auto text-[10px] text-emerald-300">
                テスト予約
              </span>
            </div>

            {/* 2〜5週目はとりあえず数字だけ埋める */}
            {Array.from({ length: 29 }).map((_, i) => {
              const day = i + 3; // 3〜31
              const isToday = day === 11; // 適当に「今日」っぽい日
              return (
                <div
                  key={day}
                  className={`h-20 rounded-lg border border-slate-800/60 bg-slate-900/40 p-1 flex flex-col items-end ${
                    isToday ? "border-emerald-400/80" : ""
                  }`}
                >
                  <span
                    className={`text-xs ${
                      isToday ? "text-emerald-300 font-semibold" : "text-slate-300"
                    }`}
                  >
                    {day}
                  </span>
                </div>
              );
            })}
          </div>
        </section>

        <p className="mt-4 text-xs text-slate-400">
          本番では、このマス目をクリックしたら予約モーダルを開いたり、API から予定を埋めたりします。
        </p>
      </main>
    </div>
  );
}