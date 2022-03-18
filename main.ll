@.str = private unnamed_addr constant [3 x i8] c"%d\00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  ;int adressen aanmaken
  %a = alloca i32, align 4
  %b = alloca i32, align 4
  %c = alloca i32, align 4

  ;laad 5 in %a
  store i32 5, i32* %a, align 4

  ;laad 6 in %b
  store i32 6, i32* %b, align 4

  store i32 19, i32* %a, align 4

  ;laad de waarde van %a in %d
  %d = load i32, i32* %a, align 4
  ;laad de waarde van %b in %e
  %e = load i32, i32* %b, align 4

  ;tel %d en %e op
  %g = add i32 %d, %e

  store i32 %g, i32* %c, align 4

  %h = load i32, i32* %c, align 4
  %i = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i64 0, i64 0), i32 %h)

  ret i32 0
}

declare dso_local i32 @printf(i8*, ...) #1
