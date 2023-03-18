// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "IWebsocket.h"
#include "MyGameInstance.generated.h"

/**
 * 
 */
UCLASS()
class MYPROJ2_API UMyGameInstance : public UGameInstance
{
	GENERATED_BODY()
public:
	virtual void Init() override;
	virtual void Shutdown() override;
	FString s;
	FString h;
	TSharedPtr<IWebSocket>WebSocket;
	
	
};
