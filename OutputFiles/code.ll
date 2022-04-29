
@.uniqprintStringuniqmain112 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.uniqprintStringmain3 = private unnamed_addr constant [11 x i8] c"%d; %d; %d\00", align 1
@.uniqprintStringmain3 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [11 x i8] c"%d; %f; %c\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [11 x i8] c"%d; %f; %c\00", align 1
@.uniqprintStringuniqmain55 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.uniqprintStringuniqmain53 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.uniqprintStringmain3 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.uniqprintStringmain5 = private unnamed_addr constant [7 x i8] c"%d; %d\00", align 1
@.uniqscanStringmain2 = private unnamed_addr constant [5 x i8] c"%d%d\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [19 x i8] c"Enter two numbers:\00", align 1
@.uniqprintStringmain4 = private unnamed_addr constant [7 x i8] c"%d%f%c\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [15 x i8] c"Hello World!\n\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1
@.uniqprintStringuniqmain19 = private unnamed_addr constant [15 x i8] c"Hello world!\n\00", align 1
@.uniqprintStringuniqmain18 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.uniqprintStringuniqmain28 = private unnamed_addr constant [15 x i8] c"Hello world!\n\00", align 1
@.uniqprintStringuniqmain18 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.uniqprintStringuniqmain18 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1
@.uniqprintStringmain14 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain11 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain8 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain5 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringuniqmain18 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1
@.uniqprintStringmain11 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain8 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain5 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain26 = private unnamed_addr constant [5 x i8] c"%f; \00", align 1
@.uniqprintStringmain23 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain19 = private unnamed_addr constant [5 x i8] c"%f; \00", align 1
@.uniqprintStringmain16 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain12 = private unnamed_addr constant [5 x i8] c"%f; \00", align 1
@.uniqprintStringmain9 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.uniqprintStringmain5 = private unnamed_addr constant [5 x i8] c"%f; \00", align 1
@.uniqprintStringmain2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain1main3 = load i32, i32* %uniqprintTempmain1, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain2, i64 0, i64 0) , i32 %uniquniqprintTempmain1main3)
	%uniqprintTempmain4 = alloca float, align 4
	store float 0x4024000000000000, float* %uniqprintTempmain4, align 4
	%uniquniqprintTempmain4main6 = load float, float* %uniqprintTempmain4, align 4
	%uniqmain7 = fpext float %uniquniqprintTempmain4main6 to double
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , double %uniqmain7)
	%uniqprintTempmain8 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain8, align 4
	%uniquniqprintTempmain8main10 = load i32, i32* %uniqprintTempmain8, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain9, i64 0, i64 0) , i32 %uniquniqprintTempmain8main10)
	%uniqprintTempmain11 = alloca float, align 4
	store float 0x4024000000000000, float* %uniqprintTempmain11, align 4
	%uniquniqprintTempmain11main13 = load float, float* %uniqprintTempmain11, align 4
	%uniqmain14 = fpext float %uniquniqprintTempmain11main13 to double
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain12, i64 0, i64 0) , double %uniqmain14)
	%uniqprintTempmain15 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain15, align 4
	%uniquniqprintTempmain15main17 = load i32, i32* %uniqprintTempmain15, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain16, i64 0, i64 0) , i32 %uniquniqprintTempmain15main17)
	%uniqprintTempmain18 = alloca float, align 4
	store float 0x4024000000000000, float* %uniqprintTempmain18, align 4
	%uniquniqprintTempmain18main20 = load float, float* %uniqprintTempmain18, align 4
	%uniqmain21 = fpext float %uniquniqprintTempmain18main20 to double
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain19, i64 0, i64 0) , double %uniqmain21)
	%uniqprintTempmain22 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain22, align 4
	%uniquniqprintTempmain22main24 = load i32, i32* %uniqprintTempmain22, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain23, i64 0, i64 0) , i32 %uniquniqprintTempmain22main24)
	%uniqprintTempmain25 = alloca float, align 4
	store float 0x4024000000000000, float* %uniqprintTempmain25, align 4
	%uniquniqprintTempmain25main27 = load float, float* %uniqprintTempmain25, align 4
	%uniqmain28 = fpext float %uniquniqprintTempmain25main27 to double
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain26, i64 0, i64 0) , double %uniqmain28)
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 7, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain1main3 = load i32, i32* %uniqprintTempmain1, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain2, i64 0, i64 0) , i32 %uniquniqprintTempmain1main3)
	%uniqprintTempmain4 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain4, align 4
	%uniquniqprintTempmain4main6 = load i32, i32* %uniqprintTempmain4, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , i32 %uniquniqprintTempmain4main6)
	%uniqprintTempmain7 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain7, align 4
	%uniquniqprintTempmain7main9 = load i32, i32* %uniqprintTempmain7, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain8, i64 0, i64 0) , i32 %uniquniqprintTempmain7main9)
	%uniqprintTempmain10 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain10, align 4
	%uniquniqprintTempmain10main12 = load i32, i32* %uniqprintTempmain10, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain11, i64 0, i64 0) , i32 %uniquniqprintTempmain10main12)
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%i = alloca i32, align 4
	store i32 0, i32* %i, align 4
br label %whileCondition_uniqmain1

whileCondition_uniqmain1:
	%uniqwhileLoopConditionuniqmain11 = alloca i32, align 4
	%uniquniqmain12 = alloca i32, align 4
	store i32 10, i32* %uniquniqmain12, align 4
	%uniqiuniqmain13 = load i32, i32* %i, align 4
	%uniquniquniqmain12uniqmain14 = load i32, i32* %uniquniqmain12, align 4
	%uniquniqmain15 = icmp slt i32 %uniqiuniqmain13, %uniquniquniqmain12uniqmain14
	%uniquniqmain16= zext i1 %uniquniqmain15 to i32
	store i32 %uniquniqmain16, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%uniqcheckValueReguniqmain17 = load i32, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%conditionValueuniqmain1= icmp eq i32 %uniqcheckValueReguniqmain17, 1
	br i1 %conditionValueuniqmain1, label %whileLoop_uniqmain1, label %endwhile_uniqmain1

whileLoop_uniqmain1:
	%uniqiuniqmain19 = load i32, i32* %i, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringuniqmain18, i64 0, i64 0) , i32 %uniqiuniqmain19)
	%uniqwhileLoopConditionuniquniqmain1101 = alloca i32, align 4
	%uniquniquniqmain1102 = alloca i32, align 4
	store i32 5, i32* %uniquniquniqmain1102, align 4
	%uniqiuniquniqmain1103 = load i32, i32* %i, align 4
	%uniquniquniquniqmain1102uniquniqmain1104 = load i32, i32* %uniquniquniqmain1102, align 4
	%uniquniquniqmain1105 = icmp eq i32 %uniqiuniquniqmain1103, %uniquniquniquniqmain1102uniquniqmain1104
	%uniquniquniqmain1106= zext i1 %uniquniquniqmain1105 to i32
	store i32 %uniquniquniqmain1106, i32* %uniqwhileLoopConditionuniquniqmain1101, align 4
	%uniqcheckValueReguniquniqmain1107 = load i32, i32* %uniqwhileLoopConditionuniquniqmain1101, align 4
	%conditionValueuniquniqmain110= icmp eq i32 %uniqcheckValueReguniquniqmain1107, 1
	br i1 %conditionValueuniquniqmain110, label %ifStatement_uniquniqmain110, label %elseStatement_uniquniqmain110

ifStatement_uniquniqmain110:
	br label %endwhile_uniqmain1
	br label %endIfElseStatement_uniquniqmain110

elseStatement_uniquniqmain110:
	%uniquniquniqmain1108 = alloca i32, align 4
	store i32 1, i32* %uniquniquniqmain1108, align 4
	%uniqiuniquniqmain1109 = load i32, i32* %i, align 4
	%uniquniquniquniqmain1108uniquniqmain11010 = load i32, i32* %uniquniquniqmain1108, align 4
	%uniquniquniqmain11011 = add i32 %uniqiuniquniqmain1109, %uniquniquniquniqmain1108uniquniqmain11010
	store i32 %uniquniquniqmain11011, i32* %i, align 4
	br label %whileCondition_uniqmain1
	br label %endIfElseStatement_uniquniqmain110

endIfElseStatement_uniquniqmain110:
	store i32 10, i32* %i, align 4
	br label %whileCondition_uniqmain1

endwhile_uniqmain1:
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 1, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain1main3 = load i32, i32* %uniqprintTempmain1, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain2, i64 0, i64 0) , i32 %uniquniqprintTempmain1main3)
	%uniqprintTempmain4 = alloca i32, align 4
	store i32 0, i32* %uniqprintTempmain4, align 4
	%uniquniqprintTempmain4main6 = load i32, i32* %uniqprintTempmain4, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , i32 %uniquniqprintTempmain4main6)
	%uniqprintTempmain7 = alloca i32, align 4
	store i32 1, i32* %uniqprintTempmain7, align 4
	%uniquniqprintTempmain7main9 = load i32, i32* %uniqprintTempmain7, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain8, i64 0, i64 0) , i32 %uniquniqprintTempmain7main9)
	%uniqprintTempmain10 = alloca i32, align 4
	store i32 0, i32* %uniqprintTempmain10, align 4
	%uniquniqprintTempmain10main12 = load i32, i32* %uniqprintTempmain10, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain11, i64 0, i64 0) , i32 %uniquniqprintTempmain10main12)
	%uniqprintTempmain13 = alloca float, align 4
	store float 0x3ff0000000000000, float* %uniqprintTempmain13, align 4
	%uniquniqprintTempmain13main15 = load float, float* %uniqprintTempmain13, align 4
	%uniqmain16 = fpext float %uniquniqprintTempmain13main15 to double
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain14, i64 0, i64 0) , double %uniqmain16)
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 0, i32* %x, align 4
	%xp = alloca i32*, align 8
	store i32* %x, i32** %xp, align 8
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca float, align 4
	store float 0x3fe0000000000000, float* %x, align 4
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%a = alloca i32, align 4
	store i32 0, i32* %a, align 4
br label %whileCondition_uniqmain1

whileCondition_uniqmain1:
	%uniqwhileLoopConditionuniqmain11 = alloca i32, align 4
	%uniquniqmain12 = alloca i32, align 4
	store i32 10, i32* %uniquniqmain12, align 4
	%uniqauniqmain13 = load i32, i32* %a, align 4
	%uniquniquniqmain12uniqmain14 = load i32, i32* %uniquniqmain12, align 4
	%uniquniqmain15 = icmp slt i32 %uniqauniqmain13, %uniquniquniqmain12uniqmain14
	%uniquniqmain16= zext i1 %uniquniqmain15 to i32
	store i32 %uniquniqmain16, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%uniqcheckValueReguniqmain17 = load i32, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%conditionValueuniqmain1= icmp eq i32 %uniqcheckValueReguniqmain17, 1
	br i1 %conditionValueuniqmain1, label %whileLoop_uniqmain1, label %endwhile_uniqmain1

whileLoop_uniqmain1:
	%uniqauniqmain19 = load i32, i32* %a, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringuniqmain18, i64 0, i64 0) , i32 %uniqauniqmain19)
	%uniquniqmain110 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain110, align 4
	%uniqauniqmain111 = load i32, i32* %a, align 4
	%uniquniquniqmain110uniqmain112 = load i32, i32* %uniquniqmain110, align 4
	%uniquniqmain113 = add i32 %uniqauniqmain111, %uniquniquniqmain110uniqmain112
	store i32 %uniquniqmain113, i32* %a, align 4
	br label %whileCondition_uniqmain1

endwhile_uniqmain1:
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 5, i32* %x, align 4
	%uniqwhileLoopConditionuniqmain11 = alloca i32, align 4
	%uniquniqmain12 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain12, align 4
	%uniqxuniqmain13 = load i32, i32* %x, align 4
	%uniquniquniqmain12uniqmain14 = load i32, i32* %uniquniqmain12, align 4
	%uniquniqmain15 = icmp slt i32 %uniqxuniqmain13, %uniquniquniqmain12uniqmain14
	%uniquniqmain16= zext i1 %uniquniqmain15 to i32
	store i32 %uniquniqmain16, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%uniqcheckValueReguniqmain17 = load i32, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%conditionValueuniqmain1= icmp eq i32 %uniqcheckValueReguniqmain17, 1
	br i1 %conditionValueuniqmain1, label %ifStatement_uniqmain1, label %elseStatement_uniqmain1

ifStatement_uniqmain1:
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.uniqprintStringuniqmain18, i64 0, i64 0) )
	br label %endIfElseStatement_uniqmain1

elseStatement_uniqmain1:
	br label %endIfElseStatement_uniqmain1

endIfElseStatement_uniqmain1:
	%uniqwhileLoopConditionuniqmain21 = alloca i32, align 4
	%uniquniqmain22 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain22, align 4
	%uniqxuniqmain23 = load i32, i32* %x, align 4
	%uniquniquniqmain22uniqmain24 = load i32, i32* %uniquniqmain22, align 4
	%uniquniqmain25 = icmp sge i32 %uniqxuniqmain23, %uniquniquniqmain22uniqmain24
	%uniquniqmain26= zext i1 %uniquniqmain25 to i32
	store i32 %uniquniqmain26, i32* %uniqwhileLoopConditionuniqmain21, align 4
	%uniqcheckValueReguniqmain27 = load i32, i32* %uniqwhileLoopConditionuniqmain21, align 4
	%conditionValueuniqmain2= icmp eq i32 %uniqcheckValueReguniqmain27, 1
	br i1 %conditionValueuniqmain2, label %ifStatement_uniqmain2, label %elseStatement_uniqmain2

ifStatement_uniqmain2:
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.uniqprintStringuniqmain28, i64 0, i64 0) )
	br label %endIfElseStatement_uniqmain2

elseStatement_uniqmain2:
	br label %endIfElseStatement_uniqmain2

endIfElseStatement_uniqmain2:
	%uniqwhileLoopConditionuniqmain31 = alloca i32, align 4
	%uniquniqmain32 = alloca i32, align 4
	%uniquniqmain33 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain33, align 4
	%uniqxuniqmain34 = load i32, i32* %x, align 4
	%uniquniquniqmain33uniqmain35 = load i32, i32* %uniquniqmain33, align 4
	%uniquniqmain36 = icmp eq i32 %uniqxuniqmain34, %uniquniquniqmain33uniqmain35
	%uniquniqmain37= zext i1 %uniquniqmain36 to i32
	store i32 %uniquniqmain37, i32* %uniquniqmain32, align 4
	%uniquniqmain38 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain38, align 4
	%uniquniquniqmain32uniqmain39 = load i32, i32* %uniquniqmain32, align 4
	%uniquniquniqmain38uniqmain310 = load i32, i32* %uniquniqmain38, align 4
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 5, i32* %x, align 4
	%uniqwhileLoopConditionuniqmain11 = alloca i32, align 4
	%uniquniqmain12 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain12, align 4
	%uniqxuniqmain13 = load i32, i32* %x, align 4
	%uniquniquniqmain12uniqmain14 = load i32, i32* %uniquniqmain12, align 4
	%uniquniqmain15 = icmp slt i32 %uniqxuniqmain13, %uniquniquniqmain12uniqmain14
	%uniquniqmain16= zext i1 %uniquniqmain15 to i32
	store i32 %uniquniqmain16, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%uniqcheckValueReguniqmain17 = load i32, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%conditionValueuniqmain1= icmp eq i32 %uniqcheckValueReguniqmain17, 1
	br i1 %conditionValueuniqmain1, label %ifStatement_uniqmain1, label %elseStatement_uniqmain1

ifStatement_uniqmain1:
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.uniqprintStringuniqmain18, i64 0, i64 0) )
	br label %endIfElseStatement_uniqmain1

elseStatement_uniqmain1:
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.uniqprintStringuniqmain19, i64 0, i64 0) )
	br label %endIfElseStatement_uniqmain1

endIfElseStatement_uniqmain1:
	%uniqwhileLoopConditionuniqmain21 = alloca i32, align 4
	%uniquniqmain22 = alloca i32, align 4
	%uniquniqmain23 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain23, align 4
	%uniqxuniqmain24 = load i32, i32* %x, align 4
	%uniquniquniqmain23uniqmain25 = load i32, i32* %uniquniqmain23, align 4
	%uniquniqmain26 = icmp eq i32 %uniqxuniqmain24, %uniquniquniqmain23uniqmain25
	%uniquniqmain27= zext i1 %uniquniqmain26 to i32
	store i32 %uniquniqmain27, i32* %uniquniqmain22, align 4
	%uniquniqmain28 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain28, align 4
	%uniquniquniqmain22uniqmain29 = load i32, i32* %uniquniqmain22, align 4
	%uniquniquniqmain28uniqmain210 = load i32, i32* %uniquniqmain28, align 4
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 5, i32* %x, align 4
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 1, i32* %x, align 4
	%uniqxmain2 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringmain1, i64 0, i64 0) , i32 %uniqxmain2)
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define void @f(i32* %parametera) #0 {
	%a = alloca i32*, align 8
	store i32* %parametera, i32** %a, align 8
	%a = alloca i32*, align 8
	ret void
}
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 0, i32* %x, align 4
	%xp = alloca i32*, align 8
	store i32* %x, i32** %xp, align 8
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.uniqprintStringmain1, i64 0, i64 0) )
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqprintTempmain1 = alloca i32, align 4
	store i32 10, i32* %uniqprintTempmain1, align 4
	%uniqprintTempmain2 = alloca float, align 4
	store float 0x3fe0000000000000, float* %uniqprintTempmain2, align 4
	%uniqprintTempmain3 = alloca i8, align 1
	store i8 37, i8* %uniqprintTempmain3, align 1
	%uniquniqprintTempmain1main5 = load i32, i32* %uniqprintTempmain1, align 4
	%uniquniqprintTempmain2main6 = load float, float* %uniqprintTempmain2, align 4
	%uniqmain7 = fpext float %uniquniqprintTempmain2main6 to double
	%uniquniqprintTempmain3main8 = load i8, i8* %uniqprintTempmain3, align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.uniqprintStringmain4, i64 0, i64 0) , i32 %uniquniqprintTempmain1main5, double %uniqmain7, i8 %uniquniqprintTempmain3main8)
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	%y = alloca i32, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([19 x i8], [19 x i8]* @.uniqprintStringmain1, i64 0, i64 0) )
	%uniqxmain3 = load i32, i32* %x, align 4
	%uniqymain4 = load i32, i32* %y, align 4
	call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqscanStringmain2, i64 0, i64 0), i32* %x, i32* %y)
	%uniqxmain6 = load i32, i32* %x, align 4
	%uniqymain7 = load i32, i32* %y, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.uniqprintStringmain5, i64 0, i64 0) , i32 %uniqxmain6, i32 %uniqymain7)
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
	%x = alloca i32, align 4
	store i32 10, i32* %x, align 4
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%uniqxmain2 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringmain1, i64 0, i64 0) , i32 %uniqxmain2)
	%x = alloca i32, align 4
	store i32 20, i32* %x, align 4
	%uniqxmain4 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringmain3, i64 0, i64 0) , i32 %uniqxmain4)
	store i32 30, i32* %x, align 4
	%uniqwhileLoopConditionuniqmain51 = alloca i32, align 4
	store i32 1, i32* %uniqwhileLoopConditionuniqmain51, align 4
	%uniqcheckValueReguniqmain52 = load i32, i32* %uniqwhileLoopConditionuniqmain51, align 4
	%conditionValueuniqmain5= icmp eq i32 %uniqcheckValueReguniqmain52, 1
	br i1 %conditionValueuniqmain5, label %ifStatement_uniqmain5, label %elseStatement_uniqmain5

ifStatement_uniqmain5:
	%uniqxuniqmain54 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringuniqmain53, i64 0, i64 0) , i32 %uniqxuniqmain54)
	%x = alloca i32, align 4
	store i32 40, i32* %x, align 4
	%uniqxuniqmain56 = load i32, i32* %x, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringuniqmain55, i64 0, i64 0) , i32 %uniqxuniqmain56)
	br label %endIfElseStatement_uniqmain5

elseStatement_uniqmain5:
	br label %endIfElseStatement_uniqmain5

endIfElseStatement_uniqmain5:
	ret i32 1
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 5, i32* %x, align 4
	%y = alloca float, align 4
	store float 0x3fe0000000000000, float* %y, align 4
	%c = alloca i8, align 1
	store i8 99, i8* %c, align 1
	%uniqxmain2 = load i32, i32* %x, align 4
	%uniqymain3 = load float, float* %y, align 4
	%uniqmain4 = fpext float %uniqymain3 to double
	%uniqcmain5 = load i8, i8* %c, align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.uniqprintStringmain1, i64 0, i64 0) , i32 %uniqxmain2, double %uniqmain4, i8 %uniqcmain5)
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 5, i32* %x, align 4
	%y = alloca float, align 4
	store float 0x3fe0000000000000, float* %y, align 4
	%c = alloca i8, align 1
	store i8 99, i8* %c, align 1
	%uniqxmain2 = load i32, i32* %x, align 4
	%uniqymain3 = load float, float* %y, align 4
	%uniqmain4 = fpext float %uniqymain3 to double
	%uniqcmain5 = load i8, i8* %c, align 1
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.uniqprintStringmain1, i64 0, i64 0) , i32 %uniqxmain2, double %uniqmain4, i8 %uniqcmain5)
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 10, i32* %x, align 4
	%xp = alloca i32*, align 8
	store i32* %x, i32** %xp, align 8
	%uniqxppointerToValuemain10 = load i32*, i32** %xp, align 8
	%uniqxppointerToValuemain1 = load i32, i32* %uniqxppointerToValuemain10, align 8
	%uniqxppointerToValuemain2 = alloca i32, align 4
	store i32 %uniqxppointerToValuemain1, i32* %uniqxppointerToValuemain2, align 4
	%uniquniqxppointerToValuemain2main4 = load i32, i32* %uniqxppointerToValuemain2, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.uniqprintStringmain3, i64 0, i64 0) , i32 %uniquniqxppointerToValuemain2main4)
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%x = alloca i32, align 4
	store i32 10, i32* %x, align 4
	%y = alloca i32, align 4
	%uniqxmain1 = load i32, i32* %x, align 4
	store i32 %uniqxmain1, i32* %y, align 4
	%z = alloca i32, align 4
	%uniqxmain2 = load i32, i32* %x, align 4
	store i32 %uniqxmain2, i32* %z, align 4
	%uniqxmain4 = load i32, i32* %x, align 4
	%uniqymain5 = load i32, i32* %y, align 4
	%uniqzmain6 = load i32, i32* %z, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.uniqprintStringmain3, i64 0, i64 0) , i32 %uniqxmain4, i32 %uniqymain5, i32 %uniqzmain6)
	ret i32 0
}
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%i = alloca i32, align 4
	store i32 0, i32* %i, align 4
br label %whileCondition_uniqmain1

whileCondition_uniqmain1:
	%uniqwhileLoopConditionuniqmain11 = alloca i32, align 4
	%uniquniqmain12 = alloca i32, align 4
	store i32 5, i32* %uniquniqmain12, align 4
	%uniqiuniqmain13 = load i32, i32* %i, align 4
	%uniquniquniqmain12uniqmain14 = load i32, i32* %uniquniqmain12, align 4
	%uniquniqmain15 = icmp slt i32 %uniqiuniqmain13, %uniquniquniqmain12uniqmain14
	%uniquniqmain16= zext i1 %uniquniqmain15 to i32
	store i32 %uniquniqmain16, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%uniqcheckValueReguniqmain17 = load i32, i32* %uniqwhileLoopConditionuniqmain11, align 4
	%conditionValueuniqmain1= icmp eq i32 %uniqcheckValueReguniqmain17, 1
	br i1 %conditionValueuniqmain1, label %whileLoop_uniqmain1, label %endwhile_uniqmain1

whileLoop_uniqmain1:
	%uniquniqmain18 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain18, align 4
	%uniqiuniqmain19 = load i32, i32* %i, align 4
	%uniquniquniqmain18uniqmain110 = load i32, i32* %uniquniqmain18, align 4
	%uniquniqmain111 = add i32 %uniqiuniqmain19, %uniquniquniqmain18uniqmain110
	store i32 %uniquniqmain111, i32* %i, align 4
	%uniqiuniqmain113 = load i32, i32* %i, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringuniqmain112, i64 0, i64 0) , i32 %uniqiuniqmain113)
	br label %whileCondition_uniqmain1

endwhile_uniqmain1:
	ret i32 1
}